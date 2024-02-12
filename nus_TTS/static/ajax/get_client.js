
$("#parent_data").change(function () {
    const parentId = $(this).val();
    console.log(parentId);
    $.ajax({
        type: "POST",
        url: '/client_data',
        data: {
            'parentId': parentId,
            'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
        },
//        console.log(data);
        success: function (data) {
            let html_data = '<option value="">Select Client</option>';
            data.forEach(function (data) {
            console.log(data);
                html_data += `<option value="${data.id}">${data.client}</option>`
            });
            $("#clients").html(html_data);
        }
    });
});




