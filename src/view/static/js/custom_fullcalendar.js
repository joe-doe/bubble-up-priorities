function new_fullCalendar(data_source) {

        $.getScript('/static/node_modules/moment/moment.js', function(){
            $.getScript('/static/node_modules/fullcalendar/dist/fullcalendar.min.js', function(){
                $('.main-body-container').fullCalendar({
                    height: 750,
                    eventSources: [
                        {
                            url: data_source
                        }
                    ],
                    header: {
                        left: 'prev,next today',
                        center: 'title',
                        right: 'month,agendaWeek,agendaDay'
                    },
                    selectable: true,
                    selectHelper: true,
                    editable: true,
                    eventLimit: true, // allow "more" link when too many events,

                    select: function(start, end, allDay) {
                        var title = prompt('Event Title: ');

                        if (title) {
                            var new_event = {
                                        title: title,
                                        start: start.format(),
                                        end: end.format(),
                                        allDay: true
                            }
                            console.log(new_event);

                            $('.main-body-container').fullCalendar('renderEvent',
                                                                    new_event,
                                                                    true // make the event "stick"
                                                                );
                            insert_event(new_event);
                        }
                        $('.main-body-container').fullCalendar('unselect');
                    },
                    eventDrop: function(event, delta, revertFunc) {
                                    if (!confirm(event.title + " was dropped on " + event.start.format()+"\nAre you sure about this change?")) {
                                        revertFunc();
                                    }
                                    update_event(event);
                                    console.log(event);
                                    console.log(delta);
                   }
                });
            });
        });

        function insert_event(new_event){
            /**
             * ajax call to store event in DB
            */
            $.ajax({
                type: 'post',
                url: '/api/events/add',
                contentType: "application/json",
                data: JSON.stringify(new_event)
            })
            .done(function(d) {
                alert("New event registered successfully");
            })
            .fail(function(a, b, c) {
                alert( "error: "+b+"\ndetails: "+c );
            });

        }

        function update_event(new_event){
            /**
             * ajax call to store event in DB
            */
            $.ajax({
                type: 'post',
                url: '/api/events/update',
                contentType: "application/json",
                data: JSON.stringify(new_event)
            })
            .done(function(d) {
                alert("New event registered successfully");
            })
            .fail(function(a, b, c) {
                alert( "error: "+b+"\ndetails: "+c );
            });

        }

        function delete_event(event){
            /**
             * ajax call to store event in DB
            */
            $.ajax({
                type: 'post',
                url: '/api/events/delete',
                contentType: "application/json",
                data: JSON.stringify(new_event)
            })
            .done(function(d) {
                alert("New event registered successfully");
            })
            .fail(function(a, b, c) {
                alert( "error: "+b+"\ndetails: "+c );
            });

        }
}
//@ sourceURL=custom_fullcalendar.js