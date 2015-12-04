$(function () {
    $("#menu-toggle").click(function(e) {
        e.preventDefault();
        $("#wrapper").toggleClass("toggled");
    });

    $('.sidebar-nav li').click(function(e) {
        var d = $('.side-body').load($(this).find('a').attr('href'));
        e.preventDefault();
    });
});