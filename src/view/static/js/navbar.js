$(function () {

    var ac = $(".side-menu-container ul").find(".active");
    var tmp =$('.side-body').load(ac.find('a').attr('href'));

    $('.navbar-toggle').click(function () {
        $('.navbar-nav').toggleClass('slide-in');
        $('.side-body').toggleClass('body-slide-in');
        $('#search').removeClass('in').addClass('collapse').slideUp(200);

        /// uncomment code for absolute positioning tweek see top comment in css
        $('.absolute-wrapper').toggleClass('slide-in');

    });

   // Remove menu for searching
   $('#search-trigger').click(function () {
        $('.navbar-nav').removeClass('slide-in');
        $('.side-body').removeClass('body-slide-in');

        /// uncomment code for absolute positioning tweek see top comment in css
        $('.absolute-wrapper').removeClass('slide-in');

    });

    $('.side-menu-container li').click(function(e) {
        $(".side-menu-container ul").find(".active").removeClass("active");
        $(this).addClass("active");
        var d = $('.side-body').load($(this).find('a').attr('href'));
        e.preventDefault();
    });

});