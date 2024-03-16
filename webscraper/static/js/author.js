var currentSwitch = 1;

function switchContent() {
    var image = document.getElementById("image");
    var heading = document.getElementById("about-heading");
    var content = document.getElementById("content");
    var container = document.getElementById("about-me-card");

    container.style.transform = "translateX(120%)";

    setTimeout(function () {
        switch (currentSwitch) {
            case 1:
                image.src = "static/img/lutowanie.webp";
                image.alt = "p3";
                image.style.objectFit = "cover";
                heading.innerText = "My hobby";
                content.innerHTML =
                    "<p>For a hudge part of my life it was Ice Hockey, for twelve years to be exact, but recent years it was programming.</p> <p>I specialize myself in Java mainly web applications in Spring boot with use of Angular framework.</p> <p>Away from programing I also love thinkering in any sort of electronics, soldering or developing small applications for microcontrollers.</p>";
                currentSwitch = 2;
                break;
            case 2:
                image.src = "static/img/Pieczec_uek.png";
                image.alt = "UEK Logo";
                image.style.objectFit = "fill";
                heading.innerText = "About me";
                content.innerHTML =
                    "<p>My name is Kacper Mila, i'm on the first year of applied informatics.</p><p>Why applied informatics? I guess because it's a good way to develp further knowlage about my field of intrests and work.</p><p>in addition to studying, I work as a junior software developer for a major company involved in, among other things, voice communication in the field. </p>";
                currentSwitch = 1;
                break;
        }

        container.style.transform = "translateX(0)";
    }, 500);
}
