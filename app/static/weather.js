
function init() {
    send_coords()
}

function load_weather() {
    // var weather = fetch('/get_weather').then(response =>  response.json()).then((data) => {
    //     console.log(data);
    //     document.getElementById('weather_dt').innerHTML = data.dt;
    //     document.getElementById('weather_temp').innerHTML = data.main.temp;
    //     document.getElementById('weather_pressure').innerHTML = data.main.pressure;
    //     document.getElementById('weather_windspeed').innerHTML = data.wind.speed;
    //     document.getElementById('weather_winddeg').innerHTML = data.wind.deg;
    // })
}

function send_coords() {
    navigator.geolocation.getCurrentPosition((position) => {
        let lat = position.coords.latitude;
        let lon = position.coords.longitude;

        fetch("/coords", {
            method: "POST",
            body: JSON.stringify({
                lat: lat,
                lon: lon
            }),
            headers: {
                "Content-type": "application/json; charset=UTF-8"
            }
        }).then((response)=>{
            load_weather();
        })

    });
}

init();