
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
        success: function (data) {
            let html_data = '<option value="">Select Client</option>';
            data.forEach(function (data) {
                html_data += `<option value="${data.id}">${data.client}</option>`
            });
            $("#client").html(html_data);
        }
    });
});




