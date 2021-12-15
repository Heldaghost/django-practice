$('.col_fav').click(function () {
    if ($(this).attr('class') === 'col_fav col-5 btn btn-dark') {
        $(this).attr('class', 'col_fav col-5 btn btn-outline-secondary')

    } else {
        $(this).attr('class', 'col_fav col-5 btn btn-dark')
    }
    var col_id = $(this).attr('id');
    $.ajax(
        {

            type: "GET",
            url: "/like_col/",
            data: {
                coll_id: col_id


            },
            success: function (data) {

            }
        })
})
;
