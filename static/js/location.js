function getLocation() {
    const locationElement = document.getElementById("location");

    // Check if geolocation is supported
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        locationElement.innerHTML = "Geolocation is not supported by your browser.";
    }
}

// Show the position (latitude and longitude)
function showPosition(position) {
    const lat = position.coords.latitude;
    const lon = position.coords.longitude;
    document.getElementById("location").innerHTML = 
        `Latitude: ${lat}<br>Longitude: ${lon}`;
}

// Handle any errors that occur during the geolocation request
function showError(error) {
    let message = "";
    switch(error.code) {
        case error.PERMISSION_DENIED:
            message = "User denied the request for Geolocation.";
            break;
        case error.POSITION_UNAVAILABLE:
            message = "Location information is unavailable.";
            break;
        case error.TIMEOUT:
            message = "The request to get user location timed out.";
            break;
        case error.UNKNOWN_ERROR:
            message = "An unknown error occurred.";
            break;
    }
    document.getElementById("location").innerHTML = message;
}