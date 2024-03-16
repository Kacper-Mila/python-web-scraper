fetch("https://meme-api.com/gimme/memes")
    .then((response) => response.json())
    .then((data) => {
        document.getElementById("meme").src = data.preview[4];
    })
    .catch((error) => {
        console.error("Error:", error);
        document.getElementById("meme").src =
            "{{ url_for('static', filename='img/og-image.webp') }}";
    });
