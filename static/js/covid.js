async function get_th() {
        var data;
        var Confirmed
        await fetch("http://185844a92011.ngrok.io/get_th_stat", requestOptions)
            .then(response => response.json())
            .then(json => {
                    Confirmed = json.Confirmed
                    document.getElementById("Confirmed Value").innerHTML = Confirmed
                        .catch(error => console.log('error', error));
                    let h11 = document.getElementById("h1top");
                    h11.innerHTML = data;
                }
            }
            var requestOptions = {
                method: 'GET',
                redirect: 'follow'
            };

        get_th()
        // var requestOptions = {
        //     method: 'GET',
        //     redirect: 'follow'
        // };

        // fetch("http://4439fc04db58.ngrok.io/get_th_stat", requestOptions)
        //     .then(response => response.text())
        //     .then(result => console.log(result))
        //     .catch(error => console.log('error', error));