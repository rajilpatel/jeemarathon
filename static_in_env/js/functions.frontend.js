//HEROTHEME MENU CONTROLLER FUNCTIONS

jQuery(function(){
    setTimeout(htheme_mm_align, 1000);
    jQuery(window).on('resize', function(){
        htheme_mm_align();
    });
});

//ALIGN MENU
function htheme_mm_align(){
    if(jQuery('.htheme_mm_holder').length > 0){
        jQuery('.htheme_mm_holder').each(function(){
            var this_offset = jQuery(this).parent('li').offset();
            var logo_offset = jQuery('.htheme_logo').offset();
            var shift = (logo_offset.left - this_offset.left);
            jQuery(this).css({
               'left':  shift + 'px'
            });
        });
    }
}