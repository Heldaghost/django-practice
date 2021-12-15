$('.view_modal').click(function () {
    var post_id;
    var myModal;
    $.ajax(
        {

            type: "GET",
            url: "/view_modal/",
            data: {
                post_id: $(this).attr('id')
            },
            success: function (data) {
                $('#modal').html(data)
                myModal = new bootstrap.Modal(document.getElementById('modal'), {
                    keyboard: false
                })
                myModal.show()
            }
        })
})
;

