async function get_info() {
    var data;
    var Temperature,Email;
    await fetch("http://158.108.182.10:3000/get_info?email=a2@gmail.com", requestOptions)
        .then(response => response.json())
        .then(json => {
            d = json.daily_temp

var tmp=[]
    for(var i=0; i<2; i++){
        console.log(i)
        tmp.push({x:new Date(d[i]["year"], d[i]["month"], d[i]["day"], d[i]["hour"], d[i]["minute"], d[i]["sec"]), y: d[i]["temp"]})
    }
window.onload = function () {
    var chart = new CanvasJS.Chart("chartContainer",
    {
    title:{
    text: "Temperature vs Time"
    },
    data: [
    {
        type: "line",

        dataPoints: tmp
    }
    ]
    })
                
    chart.render();
}
})
.catch(error => console.log('error', error));
}
var requestOptions = {
    method: 'GET',
    redirect: 'follow'
};

get_info()