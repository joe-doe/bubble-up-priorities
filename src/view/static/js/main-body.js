$(document).ready(function(){
    $.getScript('static/js/custom_fullcalendar.js', function(){
        var menu_item_name = $('.main-body-container').attr('name');
        new_fullCalendar('/api/' + menu_item_name + "/get");
    });
});
