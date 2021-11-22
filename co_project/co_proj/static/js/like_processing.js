$('.like').click(function () {
    if ($(this).attr('class') === 'like btn btn-sm btn-dark') {
        $(this).attr('class', 'like btn btn-sm btn-outline-secondary')

    } else {
        $(this).attr('class', 'like btn btn-sm btn-dark')
    }
    var post_id = $(this).attr('id');
    $.ajax(
        {

            type: "GET",
            url: "/like_post/",
            data: {
                post_id: post_id


            },
            success: function (data) {
                $('#likes_count' + post_id).text(data)


            }
        })
})
;
