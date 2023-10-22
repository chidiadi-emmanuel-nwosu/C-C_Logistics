let map;
let directionsService;
let directionsDisplay;
let pickupAutocomplete;
let deliveryAutocomplete;

function createMap () {
  const mapOptions = {
    center: { lat: 43.654, lng: -79.383 }, // center of the map to the coordinates
    zoom: 10
  };
  map = new google.maps.Map(document.getElementById('googleMap'), mapOptions);

  // infoWindow = new google.maps.InfoWindow(); // An InfoWindow is a popup window that can be used to display additional information on the map

  if (navigator.geolocation) { // if your browser geolocation is enabled
    navigator.geolocation.getCurrentPosition(function (p) { // get the users current position
      const position = {
        lat: p.coords.latitude, // store the users coordinates in a variable
        lng: p.coords.longitude
      };

      // infoWindow.setPosition(position); // set the position of the user
      // infoWindow.setContent('You!'); // set content is the text to display
      // infoWindow.open(map); // instruct infowindow to open our map
      map.setCenter(position); // sets the center of the map to the user's current position.
    }, function () {
      handleLocationError('Geolocation service failed', map.getCenter()); // if th function up fails set map to the center
    });
  } else {
    handleLocationError('No geolocation available.', map.getCenter()); // when geolocation is not enabled in the browser
  }

  directionsService = new google.maps.DirectionsService();
  directionsDisplay = new google.maps.DirectionsRenderer();
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

  // pickupAutocomplete = new google.maps.places.Autocomplete(
  //   document.getElementById('pickup_address')
  // );
  // deliveryAutocomplete = new google.maps.places.Autocomplete(
  //   document.getElementById('delivery_address')
  // );
}

// function calculateRoute () {
//   const pickup = document.getElementById('pickup_address').value;
//   const delivery = document.getElementById('delivery_address').value;

//   const routeRequest = {
//     origin: pickup,
//     destination: delivery,
//     travelMode: google.maps.TravelMode.DRIVING
//   };

//   directionsService.route(routeRequest, function (response, status) {
//     if (status === google.maps.DirectionsStatus.OK) {
//       directionsDisplay.setDirections(response);
//       displayRouteInformation(response.routes[0].legs[0]);
//     } else {
//       document.getElementById('delivery_info').innerHTML = 'Unable to calculate the route.';
//     }
//   });
// }

function handleLocationError (content, position) {
  infoWindow.setPosition(position);
  infoWindow.setContent(content);
  infoWindow.open(map);
}

// function calcRoute () {
//   const origin = document.getElementById('from').value;
//   const destination = document.getElementById('to').value;

//   const request = {
//     origin,
//     destination,
//     travelMode: google.maps.TravelMode.DRIVING
//   };

//   const directionsService = new google.maps.DirectionsService();

//   directionsService.route(request, function (result, status) {
//     if (status == google.maps.DirectionsStatus.OK) {
//       const directionsDisplay = new google.maps.DirectionsRenderer();
//       directionsDisplay.setDirections(result);
//       directionsDisplay.setMap(map);

//       // Now, make an Ajax request to your Flask route to get additional route details
//       $.ajax({
//         type: 'POST',
//         url: '/calculate_route',
//         data: {
//           pickup_address: origin,
//           delivery_address: destination
//         },
//         success: function (data) {
//           // Handle the successful response from the server
//           document.getElementById('estimated-distance').innerHTML = data.distance;
//           document.getElementById('estimated-delivery-time').innerHTML = data.duration;
//         },
//         error: function () {
//           // Handle any errors that occur during the request
//           document.getElementById('delivery-cost').innerHTML = 'Unable to retrieve route information';
//         }
//       });
//     } else {
//       document.getElementById('output').innerHTML = 'Unable to calculate route';
//     }
//   });
// }
