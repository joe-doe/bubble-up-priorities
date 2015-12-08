$(document).ready(function(){

        $.ajax({
            type: 'get',
            url: '/all_events',
            dataType: "json",
        })
        .success(function(d) {
            alert(d);
        })
        .fail(function(a, b, c) {
            alert( "error: --- "+b+" ---- <br>details: "+c );
        });

       $('.events-main-page').load('calendar');
});
