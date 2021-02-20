async function get_info() {
    var data;
    var Temperature,Email;
    await fetch("http://185844a92011.ngrok.io/get_info?email=a2@gmail.com", requestOptions)
        .then(response => response.json())
        .then(json => {
            Temperature = json.show_temp
            document.getElementById("Temperature").innerHTML = Temperature
            Email = json.email
            document.getElementById("Email").innerHTML = Email
            Blood = json.blood_type
            document.getElementById("Blood").innerHTML = Blood
            Firstname = json.firstname
            document.getElementById("Firstname").innerHTML = Firstname
            Job = json.job
            document.getElementById("Job").innerHTML = Job
            Surname = json.surname
            document.getElementById("Surname").innerHTML = Surname
        })
        .catch(error => console.log('error', error));
    }
    var requestOptions = {
        method: 'GET',
        redirect: 'follow'
    };

get_info()

window.onload = function () {

    var data;

    var dps = []; // dataPoints
    var chart = new CanvasJS.Chart("chartContainer", {
        title :{
            text: "Temperature Per 2 Hours"
        },
        data: [{
              lineColor : "darkblue",
            type: "line",
            dataPoints: dps
        }],
         axisX:{
              title: "Time"
         },
          axisY:{
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
            xVal+=2;
            yVal++;
        }
        if (dps.length > dataLength) {
            dps.shift();
        }
        chart.render();
    };
    updateChart(dataLength);
    setInterval(function(){updateChart()}, updateInterval);
    
    }