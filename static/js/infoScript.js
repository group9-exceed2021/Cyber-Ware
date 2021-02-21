let imported = document.createElement('script');
imported.src = 'https://canvasjs.com/assets/script/canvasjs.min.js';
document.head.appendChild(imported);
const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
const email = urlParams.get('email')

function get_info() {
    let requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };
    let Temperature, Email, Blood, Firstname, d, d2, Job, Surname;
    window.onload = function () {

        fetch("http://158.108.182.10:3000/get_info?email=" + email, requestOptions)
            .then(response => response.json())
            .then(json => {
                console.log(json)
                Temperature = json.show_temp
                document.getElementById("Temperature").innerHTML = Temperature

                Email = json.email
                document.getElementById("Email").innerHTML = Email

                Blood = json.blood_type
                document.getElementById("Blood").innerHTML = Blood

                Firstname = json.firstname
                document.getElementById("Firstname").innerHTML = Firstname
                document.getElementById("Firstname2").innerHTML = Firstname
                d = json.daily_temp
                d2 = json.avg

                console.log(d)
                console.log(d2)
                // document.getElementsByTagName("h3")
                // var all = document.getElement
                Job = json.job
                document.getElementById("Job").innerHTML = Job
                Surname = json.surname
                document.getElementById("Surname").innerHTML = Surname
                //console.log(d)

                console.log(123)
                let tmp = [];
                for (let i = 0; i < d.length; i++) {
                    console.log(i)
                    tmp.push({
                        x: new Date(d[i]["year"], d[i]["month"], d[i]["day"], d[i]["hour"], d[i]["minute"], d[i]["sec"]),
                        y: d[i]["temp"]
                    })
                }

                let tmp2 = [];
                for (let j = 0; j < d2.length; j++) {
                    console.log(j)
                    tmp2.push({
                        x: new Date(d2[j]["year"], d2[j]["month"], d2[j]["day"]),
                        y: d2[j]["temp_avg"]
                    })
                }

                let chart1 = new CanvasJS.Chart("chartContainer",
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
                                dataPoints: tmp
                            }
                        ]
                    });
                let chart2 = new CanvasJS.Chart("chartContainer2",
                    {
                        title: {
                            text: "Daily Average Temperature"
                        },

                        axisX: {
                            title: "Date",
                            gridThickness: 2,
                            interval: 2,
                            intervalType: "day",
                            valueFormatString: "hh TT K",
                            labelAngle: -20
                        },
                        axisY: {
                            title: "Average Temperature"
                        },
                        data: [
                            {
                                type: "line",
                                dataPoints: tmp2
                            }
                        ]
                    });


                chart1.render();
                chart2.render();
            })

            .catch(error => console.log('error', error));
    }
}

get_info();
// console.log(d)
/*
window.onload = function () {

    var data;

    var dps = []; // dataPoints
    var chart = new CanvasJS.Chart("chartContainer", {
        title: {
            text: "Temperature Per 2 Hours"
        },
        data: [{
            lineColor: "darkblue",
            type: "line",
            dataPoints: dps
        }],
        axisX: {
            title: "Time"
        },
        axisY: {
            title: "Temperature"
        }
    });

    var xVal = 0;
    var yVal = 0;
    var updateInterval = 2000;
    var dataLength = 14;

    var updateChart = function (count) {
        count = count || 1;
        for (var j = 0; j < count; j++) {
            dps.push({
                x: xVal,
                y: yVal
            });
            xVal += 2;
            yVal++;
        }
        if (dps.length > dataLength) {
            dps.shift();
        }
        chart.render();
    };
    updateChart(dataLength);
    setInterval(function () {
        updateChart()
    }, updateInterval);

}*/
