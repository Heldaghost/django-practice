$('.switch_wall').click(function () {
    var post_id;
    $.ajax(
        {
            type: "GET",
            url: "/switch_data/",
            data: {
                post_id: $(this).attr('id')
            },
            success: function (data) {

                $('#container').html(data)

            }
        })
});