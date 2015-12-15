    $(function () {
        $('#date_from').datetimepicker();
        $('#date_to').datetimepicker({
            useCurrent: false //Important! See issue #1075
        });
        $("#date_from").on("dp.change", function (e) {
            $('#date_to').data("DateTimePicker").minDate(e.date);
        });
        $("#date_to").on("dp.change", function (e) {
            $('#date_from').data("DateTimePicker").maxDate(e.date);
        });

        $(".get-dates").click(function(e){
        var event_info = $('#form').serializeJSON();

        var new_event = {
            title: event_info.name,
            description: event_info.description,
            start: $('#date_from').data("DateTimePicker").date(),
            end: $('#date_to').data("DateTimePicker").date(),
            allDay: false
        }

        $.ajax({
            type: 'post',
            url: '/api/events',
            contentType: "application/json",
            data: JSON.stringify(new_event)
        })
        .success(function(d) {
            alert(d);
        })
        .fail(function(a, b, c) {
            alert( "error: --- "+b+" ---- <br>details: "+c );
        });
        e.preventDefault();
        });
    });