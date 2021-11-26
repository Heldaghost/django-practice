$('.del_col').click(function () {
    var col_id = $(this).attr('id');
    $.ajax(
        {
            type: "GET",
            url: "/delete_cols/",
            data: {
                col_id: col_id,
            },
            success: function (data) {
                $('#container').html(data)

            }
        })
});