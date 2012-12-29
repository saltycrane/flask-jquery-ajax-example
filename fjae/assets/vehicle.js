$("#make_select").change(function() {
    var make_id = $(this).find(":selected").val();
    var request = $.ajax({
        type: 'GET',
        url: '/models/' + make_id + '/',
    });
    request.done(function(data){
        var option_list = [["", "--- Select One ---"]].concat(data);

        $("#model_select").empty();
        for (var i = 0; i < option_list.length; i++) {
            $("#model_select").append(
                $("<option></option>").attr(
                    "value", option_list[i][0]).text(option_list[i][1])
            );
        }
    });
});
