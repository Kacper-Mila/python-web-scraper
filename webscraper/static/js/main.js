document
    .getElementById("navSearchForm")
    .addEventListener("click", function (event) {
        event.preventDefault();
        var productId = document.getElementById("productId").value;
        this.action = "{{ url_for('scrape') }}/" + productId;
        this.method = "GET";
        this.submit();
    });
