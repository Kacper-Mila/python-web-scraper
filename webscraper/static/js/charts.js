const productId = document.getElementById("productid").innerText;

let cdata = {};

fetch(`/charts-data?productid=${productId}`)
    .then((response) => response.json())
    .then((data) => {
        cdata = data;

        createFirstChart();
        createSecondChart();
    })
    .catch((error) => {
        console.error("Error:", error);
    });

function createFirstChart() {
    let ctx = document.getElementById("first_Chart_id").getContext("2d");

    let chart = new Chart(ctx, {
        type: "doughnut",
        data: cdata.recommendations,
        options: {
            responsive: true,
            maintainAspectRatio: false,
        },
    });
}

function createSecondChart() {
    let ctx = document.getElementById("second_Chart_id").getContext("2d");

    let chart = new Chart(ctx, {
        type: "bar",
        data: cdata.stars,
        options: {
            responsive: true,
            maintainAspectRatio: false,
        },
    });
}
