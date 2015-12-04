$(document).ready(function(){
	$("#form").submit(function(e)
	{
        var person = $("#form").serializeJSON();
        console.log(person);

        $.ajax({
            type: 'post',
            url: '/set_user',
            contentType: "application/json",
            data: JSON.stringify(person)
        })
        .success(function(d) {
            alert(d);
        })
        .fail(function(a, b, c) {
            alert( "error "+b+" AND "+c );
        });
        e.preventDefault();
    });
});