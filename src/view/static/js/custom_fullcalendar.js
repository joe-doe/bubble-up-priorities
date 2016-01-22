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

                    select: function(from_that, to_that, allDay) {
                            $.getScript('/static/node_modules/jquery-serializejson/jquery.serializejson.min.js');
                            $.getScript('/static/node_modules/eonasdan-bootstrap-datetimepicker/build/js/bootstrap-datetimepicker.min.js', function(){
                                $('#date_from').datetimepicker();
                                $('#date_from').data("DateTimePicker").defaultDate(from_that);
                                $('#date_to').datetimepicker({
                                    useCurrent: false //Important! See issue #1075
                                });
                                $('#date_to').data("DateTimePicker").defaultDate(to_that);

                                $('#date_from').on("dp.change", function (e) {
                                    $('#date_to').data("DateTimePicker").minDate(e.date);
                                });

                                $('#date_to').on("dp.change", function (e) {
                                    $('#date_from').data("DateTimePicker").maxDate(e.date);
                                });
                            });

                            // Show modal window with event registration form
                            $( "#event-input-form" ).modal();

                            // For modal window, on close:
                            // 1. unregister click handler for registration button
                            // 2. unregister click handler for date from button
                            // 3. unregister click handler for date to button
                            // 4. unregister on handler modal window
                            // 5. clear the form
                            $("#event-input-form").on('hidden.bs.modal', function (){
                                $(".get-dates").unbind();
                                $('#date_from').unbind();
                                $('#date_to').unbind();
                                $(this).unbind();
                                $(this).find('form')[0].reset();
                            });

                            // Upon click on registration button, register the new event
                            $(".get-dates").click(function(e){
                                var event_info = $('#input-form').serializeJSON();
                                var new_event = {
                                    title: event_info.name,
                                    description: event_info.description,
                                    start: $('#date_from').data("DateTimePicker").date(),
                                    end: $('#date_to').data("DateTimePicker").date(),
                                    allDay: event_info.all_day_event == undefined ? false:true
                                }
                                $('.main-body-container').fullCalendar('renderEvent',
                                                                        new_event,
                                                                        true // make the event "stick"
                                                                    );
                                $('.main-body-container').fullCalendar('unselect');
                                insert_event(new_event);
                                e.preventDefault();
                            });
                    },
                    eventDrop: function(event, delta, revertFunc) {
                                    if (!confirm(event.title + " was dropped on " + event.start.format()+"\nAre you sure about this change?")) {
                                        revertFunc();
                                    }
                                    update_event(event);
                                    console.log(event);
                                    console.log(delta);
                     }
//                   },
//                   eventClick: function(calEvent, jsEvent, view) {
//                        alert('Event: ' + calEvent.title);
//                        alert('Coordinates: ' + jsEvent.pageX + ',' + jsEvent.pageY);
//                        alert('View: ' + view.name);
//
//                        // change the border color just for fun
//                        $(this).css('border-color', 'red');
//
//                    }
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
                alert("New event updated successfully");
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
                alert("New event deleted successfully");
            })
            .fail(function(a, b, c) {
                alert( "error: "+b+"\ndetails: "+c );
            });

        }
}
//@ sourceURL=custom_fullcalendar.js