$(function () {
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

    $('.sidebar-nav li').click(function(e) {
        var d = $('.side-body').load($(this).find('a').attr('href'));
        e.preventDefault();
    });

    $('.first-class-menu-item').click(function(e) {
       $('.side-body').load($(this).attr('href').slice(6));
        e.preventDefault();
    });

    $('.second-class-menu-item').click(function(e) {
       $('.side-body').load($(this).attr('href'));
        e.preventDefault();
    });

});