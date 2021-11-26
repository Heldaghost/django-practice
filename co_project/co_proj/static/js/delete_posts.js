$('.del').click(function () {
    var post_id = $(this).attr('id');
    $.ajax(
        {
            type: "GET",
            url: "/delete_post/",
            data: {
                post_id: post_id
            },
            success: function (data) {
                $('#container').html(data)

            }
        })
});

