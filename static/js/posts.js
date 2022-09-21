// 
// 
// 
$(function(){
    $('.js-menu-icon').click(function(){
        // $(this) : self element, namely div.js-menu-icon
        //next(): Next to div.js-menu-icon.namely div.menu
        //toggle(): Switch show and Hide
        $(this).next().toggle();

    })

})