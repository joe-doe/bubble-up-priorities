function new_fullCalendar(data_source) {

        $.getScript('/static/node_modules/moment/moment.js', function(){
            $.getScript('/static/node_modules/fullcalendar/dist/fullcalendar.min.js', function(){
                $('.main-body-container').fullCalendar({
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
                    select: function(start, end) {
                        var title = prompt('Event Title:');
                        var eventData;
                        if (title) {
                            eventData = {
                                title: title,
                                start: start,
                                end: end
                            };
                            $('#calendar').fullCalendar('renderEvent', eventData, true); // stick? = true
                        }
                        $('#calendar').fullCalendar('unselect');
                    },
                    editable: true,
                    eventLimit: true, // allow "more" link when too many events
                });
            });
        });
}