function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result)
                .show();
            var form_data = $('#blah').attr('src', e.target.result);
            $.ajax({
                type: 'POST',
                url: '/uploads',
                data: form_data,
                contentType: false,
                cache: false,
                processData: false,
                async: false,
                success: function(data) {
                    console.log('Success!');
                },
            });
            };
            $('.upload').attr('disabled','enabled')
            reader.readAsDataURL(input.files[0]);
    }
}