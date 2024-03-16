$(document).ready(function () {
    $("#productId").on("input", function () {
        var inputVal = $(this).val();
        if (inputVal.length > 0) {
            $("#navSearchButton").attr({
                "data-bs-toggle": "modal",
                "data-bs-target": "#modalLoading",
            });
        } else {
            $("#navSearchButton").removeAttr("data-bs-toggle data-bs-target");
        }
    });
});
