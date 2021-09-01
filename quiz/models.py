import random
from django.db import models
from django.db.models import F, Q, Count, Sum, Case, When
from django.db.models.functions import Cast
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from model_utils.models import TimeStampedModel
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    contact_number = models.CharField(max_length=100,null=True)
    city = models.CharField(max_length=100,null=True)
    state = models.CharField(max_length=100,null=True)
    contacted = models.BooleanField(default=False)


class Question(models.Model):
    ALLOWED_NUMBER_OF_CORRECT_CHOICES = 1

    description = models.TextField(_('Description'), default='desc', null=True)
    image = models.ImageField()
    is_published = models.BooleanField(_('Has been published?'), default=False, null=False)
    maximum_marks = models.DecimalField(_('Maximum Marks'), default=4, decimal_places=2, max_digits=6)

    def __str__(self):
        return str(self.is_published)

    def get_correct_choice(self):
        return self.choices.filter(is_correct=True).first()


class Choice(TimeStampedModel):
    MAX_CHOICES_COUNT = 4

    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    is_correct = models.BooleanField(_('Is this answer correct?'), default=False, null=False)
    html = models.TextField(_('Choice Text'))

    def __str__(self):
        return self.html


class QuizProfile(TimeStampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='user_quiz_1')
    total_score = models.DecimalField(_('Total Score'), default=0, decimal_places=2, max_digits=10)

    def __str__(self):
        return f'<QuizProfile: user={self.user}>'

    def get_new_question(self):
        used_questions_pk = AttemptedQuestion.objects.filter(quiz_profile=self).values_list('question__pk', flat=True)
        remaining_questions = Question.objects.exclude(pk__in=used_questions_pk)
        if not remaining_questions.exists():
            return
        return random.choice(remaining_questions)

    def create_attempt(self, question):
        attempted_question = AttemptedQuestion(question=question, quiz_profile=self)
        attempted_question.save()

    def evaluate_attempt(self, attempted_question, selected_choice):
        if attempted_question.question_id != selected_choice.question_id:
            return

        attempted_question.selected_choice = selected_choice
        if selected_choice.is_correct is True:
            attempted_question.is_correct = True
            attempted_question.marks_obtained = attempted_question.question.maximum_marks

        attempted_question.save()
        self.update_score()

    def update_score(self):
        marks_sum = self.attempts.filter(is_correct=True).aggregate(
            models.Sum('marks_obtained'))['marks_obtained__sum']
        self.total_score = marks_sum or 0
        self.save()

    @classmethod
    def get_rankings(cls):
        rankings = QuizProfile.objects.select_related(
            'user',
        ).annotate(
            total_attempts=Count('attempts'),
            correct_attempts=Sum(Case(When(attempts__is_correct=True, then=1), default=0, output_field=models.IntegerField())),
            success_rate=Cast(100.0 * F('correct_attempts') / F('total_attempts'), models.FloatField())
        ).order_by(
            '-total_score',
            '-correct_attempts',
            '-success_rate',
            'created'
        )
        return rankings


class AttemptedQuestion(TimeStampedModel):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    quiz_profile = models.ForeignKey(QuizProfile, on_delete=models.CASCADE, related_name='attempts')
    selected_choice = models.ForeignKey(Choice, on_delete=models.CASCADE, null=True)
    is_correct = models.BooleanField(_('Was this attempt correct?'), default=False, null=False)
    marks_obtained = models.DecimalField(_('Marks Obtained'), default=0, decimal_places=2, max_digits=6)

    def get_absolute_url(self):
        return f'/september/submission-result/{self.pk}/'
    
    def __str__(self):
        return self.quiz_profile.user.username
        
