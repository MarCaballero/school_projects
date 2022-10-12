navigator.geolocation.getCurrentPosition(displayWeather)

function displayWeather(position){
    fetch('https://api.openweathermap.org/data/2.5/weather?lat=' + position.coord)
        .then(response => {
            return response.json();
        })
        .then(data =>{
            console.log(data)
            let temp = Maath.round(data.main.temp)
            let description = data.weather[0].description
            document.getElementById("desc").innerHTML = "It is " + temp + " degrees today with " + description
            //console.log(temp + " " + description)
        })
}
