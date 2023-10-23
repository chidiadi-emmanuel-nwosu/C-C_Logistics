function createMap () {
  const mapOptions = {
    center: { lat: 43.654, lng: -79.383 }, // center of the map to the coordinates
    zoom: 10
  };
  const map = new google.maps.Map(document.getElementById('googleMap'), mapOptions);

  if (navigator.geolocation) { // if your browser geolocation is enabled
    navigator.geolocation.getCurrentPosition(function (p) { // get the users current position
      const position = {
        lat: p.coords.latitude, // store the users coordinates in a variable
        lng: p.coords.longitude
      };

      map.setCenter(position); // sets the center of the map to the user's current position.
    }, function () {
      handleLocationError('Geolocation service failed', map.getCenter()); // if th function up fails set map to the center
    });
  } else {
    handleLocationError('No geolocation available.', map.getCenter()); // when geolocation is not enabled in the browser
  }

  const directionsService = new google.maps.DirectionsService();
  const directionsDisplay = new google.maps.DirectionsRenderer();

  directionsDisplay.setMap(map);

  const routeRequest = {
    origin: pickup,
    destination: delivery,
    travelMode: google.maps.TravelMode.DRIVING
  };

  directionsService.route(routeRequest, function (response, status) {
    if (status === google.maps.DirectionsStatus.OK) {
      directionsDisplay.setDirections(response);
      // displayRouteInformation(response.routes[0].legs[0]);
    } else {
      document.getElementById('delivery_info').innerHTML = 'Unable to calculate the route.';
    }
  });

  function handleLocationError (content, position) {
    infoWindow.setPosition(position);
    infoWindow.setContent(content);
    infoWindow.open(map);
  }
}
