$(document).ready(function(){

        $.ajax({
            type: 'get',
            url: '/api/events',
            dataType: "json",
        })
        .success(function(d) {
            alert(d);
        })
        .fail(function(a, b, c) {
            alert( "error: --- "+b+" ---- \ndetails: "+c );
        });

       $('.events-main-page').load('calendar');



});
