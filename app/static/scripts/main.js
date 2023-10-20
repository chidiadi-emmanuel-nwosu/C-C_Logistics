var map, infoWindow;

function createMap () { //This function will be responsible for creating and initializing the Google Map.
  var options = {
    center: { lat: 43.654, lng: -79.383 }, //center of the map to the coordinates 
    zoom: 10
  };

  map = new google.maps.Map(document.getElementById('googleMap'), options); //It uses the google.maps.Map constructor, passing the document.getElementById('map') as the HTML element where the map should be displayed, and the options object as the initial map configuration.
 
  infoWindow = new google.maps.InfoWindow; //An InfoWindow is a popup window that can be used to display additional information on the map

  if (navigator.geolocation) { //if your browser geolocation is enabled
    navigator.geolocation.getCurrentPosition(function (p) {  //get the users current position
      var position = {
        lat: p.coords.latitude, //store the users coordinates in a variable
        lng: p.coords.longitude
      };

      infoWindow.setPosition(position); //set the position of the user
      infoWindow.setContent('You!'); //set content is the text to display
      infoWindow.open(map); //instruct infowindow to open our map
      map.setCenter(position); //sets the center of the map to the user's current position.
    }, function () {
      handleLocationError('Geolocation service failed', map.getCenter()); //if th function up fails set map to the center
    });
  } else {
    handleLocationError('No geolocation available.', map.getCenter()); //when geolocation is not enabled in the browser
  }
  var input = document.getElementById('from'); //create an input field element with an id of 'search' from our html file
  var input2 = document.getElementById('to');
  
  var searchBox = new google.maps.places.SearchBox(input); //The SearchBox is a feature of the Google Maps JavaScript API that allows users to enter location queries
  var searchBox2 = new google.maps.places.SearchBox(input2);
  map.addListener('bounds_changed', function() {
    searchBox.setBounds(map.getBounds());
    searchBox2.setBounds(map.getBounds());
  });
  /*
  The purpose of this code is to ensure that the search results displayed in the search box are relevant to the area currently visible on the map. 
  When the user interacts with the map, such as by panning or zooming, the 'bounds_changed' event is triggered, and the search box's bounds are updated accordingly. 
  This helps in providing search results that are specific to the portion of the map that the user is currently looking at, 
  enhancing the user experience and making sure that search results are related to the visible area on the map
  */

  var markers = [];
  var markers2 = [];
  
  searchBox.addListener('places_changed', function () { //This event is triggered when the user enters a location query and selects a place from the search results.
    var places = searchBox.getPlaces(); //retrieves the list of places returned by the search. The getPlaces method is used to access the results of the location search.
  
  
    if (places.length == 0)// checks if there are any places in the search results. If there are no results, the function returns early, and no markers are added to the map
      return;

    markers.forEach(function (m) { m.setMap(null); });
    markers = [];
    /*this code is used to reset the markers on the map. 
    It iterates through all the markers in the markers array and sets their association with the map to null, 
    effectively removing them from the map. After removing the markers, 
    it clears the markers array, ensuring that it's empty and ready to store new markers that will be added based on the search results. 
    This is a common practice when you want to update or replace markers on a map based on new data or user interactions.
    */
    var bounds = new google.maps.LatLngBounds(); 
    /*creates a new instance of the LatLngBounds class provided by the Google Maps JavaScript API. 
    The LatLngBounds class is used to define a bounding box for a geographical area. 
    It doesn't initially contain any coordinates; it's an empty bounding box.
    */
    
    places.forEach(function(p) { //This loop iterates through the list of places returned by the search
      if (!p.geometry) //
        return;
      /*check is to filter out any place objects that lack valid geographical coordinates or geometry information. 
      This is important because only places with valid geographical data can be displayed on the map as markers.
      */ 
      markers.push(new google.maps.Marker({
        map: map,
        title: p.name,
        position: p.geometry.location
      }));
      /*each valid place, it creates a new Google Maps marker with the place's name and position and adds it to the markers array. 
      The marker is also associated with the map.
      */
      if (p.geometry.viewport)
        bounds.union(p.geometry.viewport);
      else
        bounds.extend(p.geometry.location);
    });
    /*It updates the bounds variable based on the geometry of the place. 
    If the place has a viewport (a defined area), it extends the bounds to include the viewport. 
    If not, it extends the bounds to include the specific location of the place.
    */
    map.fitBounds(bounds); //Finally, it adjusts the map's viewport to fit all the markers within the calculated bounds. This ensures that all the markers are visible on the map
  });

  searchBox2.addListener('places_changed', function () { 
    var places2 = searchBox2.getPlaces(); 
  
    if (places2.length == 0)
      return;

    markers2.forEach(function (m) { m.setMap(null); });
    markers2 = [];
    var bounds2 = new google.maps.LatLngBounds(); 
    
    places2.forEach(function(p) { 
      if (!p.geometry) //
        return;
      markers2.push(new google.maps.Marker({
        map: map,
        title: p.name,
        position: p.geometry.location
      }));
      if (p.geometry.viewport)
        bounds2.union(p.geometry.viewport);
      else
        bounds2.extend(p.geometry.location);
    });
    map.fitBounds(bounds2); 
  });
}

function handleLocationError (content, position) {
  infoWindow.setPosition(position);
  infoWindow.setContent(content);
  infoWindow.open(map);
}
function calcRoute() {
    var origin = document.getElementById('from').value;
    var destination = document.getElementById('to').value;

    var request = {
        origin: origin,
        destination: destination,
        travelMode: google.maps.TravelMode.DRIVING
    };

    var directionsService = new google.maps.DirectionsService();

    directionsService.route(request, function (result, status) {
        if (status == google.maps.DirectionsStatus.OK) {
            var directionsDisplay = new google.maps.DirectionsRenderer();
            directionsDisplay.setDirections(result);
            directionsDisplay.setMap(map);

            // Now, make an Ajax request to your Flask route to get additional route details
            $.ajax({
                type: 'POST',
                url: '/calculate_route',
                data: {
                    'pickup_address': origin,
                    'delivery_address': destination
                },
                success: function (data) {
                    // Handle the successful response from the server
                    document.getElementById('output').innerHTML = 'Distance: ' + data.distance + '<br>';
                    document.getElementById('output').innerHTML += 'Duration: ' + data.duration + '<br>';
                },
                error: function () {
                    // Handle any errors that occur during the request
                    document.getElementById('output').innerHTML = 'Unable to retrieve route information';
                }
            });
        } else {
            document.getElementById('output').innerHTML = 'Unable to calculate route';
        }
    });
}
