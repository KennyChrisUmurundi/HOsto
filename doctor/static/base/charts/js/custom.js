(function ($) {
    "use strict"; // Start of use strict
    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
    });
    /*Loader Javascript
    -------------------*/
    var window_var = $(window);
    window_var.on('load', function () {
        $(".loading").fadeOut("fast");
        $("#snackbar").addClass("show");
    });
    // scroll to top
    $(window).on('scroll',function () {
        if ($(this).scrollTop() > 50) {
            $('#back-to-top').fadeIn();
        } else {
            $('#back-to-top').fadeOut();
        }
    });
    // scroll body to 0px on click
    $('#back-to-top').on('click',function () {
        $('body,html').animate({
            scrollTop: 0
        }, 800);
        return false;
    });
    // scroll to top End

    // theme color change
	
    // theme color change End

    // fullscreen function
    $(".fullscreen").on('click', function(){
        if(document.webkitCurrentFullScreenElement==null){
            document.documentElement.webkitRequestFullScreen();
        }else{
            document.webkitCancelFullScreen();
        }
    });
     // fullscreen function End

})(jQuery);
