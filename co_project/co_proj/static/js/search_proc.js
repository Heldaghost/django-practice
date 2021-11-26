$('#search_but').click(function () {
    let search_item = $('#dropbut').text()
    $.ajax(
        {
            type: "GET",
            url: "/search/",
            data: {
                search_item: search_item,
                search_option: $('#search_input').val()
            },
            success: function (data) {
                $('#container').html(data)

            }
        })
});