let imported = document.createElement('script');
imported.src = 'https://canvasjs.com/assets/script/canvasjs.min.js';
document.head.appendChild(imported);

window.onload = function () {
    fetch("http://158.108.182.10:3000/get_info?email=a2@gmail.com", requestOptions)
        .then(response => response.json())
        .then(json => {
            d2 = json.daily_avg
            let tmp2 = [];
            for (var i = 0; i < d2.length; i++) {
                console.log(i)
                tmp2.push({x: new Date(d2[i]["year"], d2[i]["month"], d2[i]["day"]), y: d2[i]["temp_avg"]})
            }

            let chart2 = new CanvasJS.Chart("chartContainer",
                {
                    title: {
                        text: "Temperature per 2 hours"
                    },

                    axisX: {
                        title: "Time",
                        gridThickness: 2,
                        interval: 2,
                        intervalType: "hour",
                        valueFormatString: "hh TT K",
                        labelAngle: -20
                    },
                    axisY: {
                        title: "Temperature"
                    },
                    data: [
                        {
                            type: "line",
                            dataPoints: tmp2
                        }
                    ]
                });
            chart2.render();
        })
}