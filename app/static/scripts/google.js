const pickupInput = $('#pickup_address');
const deliveryInput = $('#delivery_address');
const confirmButton = $('#confirmDelivery');

let map;
let directionsDisplay;
let directionsService;

// Initialize Google Maps with user's location as center
function initMap (userLocation) {
  map = new google.maps.Map(document.getElementById('googleMap'), {
    center: userLocation, // User's location as center
    zoom: 10
  });

  directionsDisplay = new google.maps.DirectionsRenderer();
  directionsService = new google.maps.DirectionsService();
  directionsDisplay.setMap(map);

  // Initialize Autocomplete for Pickup Address
  const pickupAutocomplete = new google.maps.places.Autocomplete(pickupInput[0]);

  // Initialize Autocomplete for Delivery Address
  const deliveryAutocomplete = new google.maps.places.Autocomplete(deliveryInput[0]);

  // Handle Confirm Delivery Button Click
  confirmButton.click(function () {
    calculateRoute();
  });
}

// Fetch the user's current location
function getUserLocation () {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
      const userLocation = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      initMap(userLocation);
    }, function () {
      alert('Failed to retrieve user location.');
      // You can handle this error as needed.
      // For now, the center will remain the default (Toronto) if geolocation fails.
      initMap({ lat: 43.653225, lng: -79.383186 });
    });
  } else {
    alert('Geolocation is not supported by your browser.');
    initMap({ lat: 43.653225, lng: -79.383186 }); // Fallback to default center
  }
}

// Calculate and Display Route
function calculateRoute () {
  const origin = pickupInput.val();
  const destination = deliveryInput.val();

  const request = {
    origin,
    destination,
    travelMode: google.maps.TravelMode.DRIVING
  };

  directionsService.route(request, function (result, status) {
    if (status === google.maps.DirectionsStatus.OK) {
      directionsDisplay.setDirections(result);
      displayRouteDetails(result);
    } else {
      alert('Unable to calculate route.');
    }
  });
}

// Display Route Details
function displayRouteDetails (route) {
  const routeSummary = route.routes[0].legs[0];
  const distance = routeSummary.distance.text;
  const duration = routeSummary.duration.text;

  // You can calculate the cost based on distance and other factors here
  const cost = calculateCost(distance);

  // Display the route, distance, duration, and cost in a popup or modal
  // For simplicity, we'll just show an alert here
  alert(`Distance: ${distance}\nDuration: ${duration}\nCost: ${cost}`);
}

// A function to calculate the cost based on distance
function calculateCost (distance) {
  // Implement your cost calculation logic here
  // This can vary based on your business rules
  // For example, you can charge a certain amount per kilometer
  return 'Your cost calculation goes here';
}

// Fetch the user's location and initialize the map
getUserLocation();
