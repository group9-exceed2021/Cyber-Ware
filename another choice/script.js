fetch()
    .then(function (response){
        return response.json()
    })
    .then(function (data){
        appendData(data) // show data
    })
    .catch(function (err){
        console.log('error: '+ err)
    })

function appendData(data){
    var mainContainer = document.getElementById("myData");
    
}