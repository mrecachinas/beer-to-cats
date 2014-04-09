function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            $('#blah')
                .attr('src', e.target.result)
                .show();
        };
        $('.upload').attr('disabled','enabled')
        reader.readAsDataURL(input.files[0]);
    }
}