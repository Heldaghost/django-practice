$('#search_but').click(function () {
    let search_item = $('#dropbut').text()
    let search_option = $('#search_input').val()
    // length > 0
    if(search_option.length > 0 ) {
        $.ajax(
            {
                type: "GET",
                url: "/search/",
                data: {
                    search_item: search_item,
                    search_option: search_option
                },
                success: function (data) {
                    $('#container').html(data)
                    $('#pagin').html('')
                }
            })
    }
});