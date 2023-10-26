function initMap () {
  // Initialize the autocomplete service for pickup and delivery inputs
  const pickupInput = document.getElementById('pickup_address');
  const deliveryInput = document.getElementById('delivery_address');
  const pickupAutocomplete = new google.maps.places.Autocomplete(pickupInput);
  const deliveryAutocomplete = new google.maps.places.Autocomplete(deliveryInput);

  // Listen for changes in the input fields
  pickupAutocomplete.addListener('place_changed', validateForm);
  deliveryAutocomplete.addListener('place_changed', validateForm);

  validateForm();

  // Function to validate the form
  function validateForm () {
    const pickupPlace = pickupAutocomplete.getPlace();
    const deliveryPlace = deliveryAutocomplete.getPlace();
    const pickupError = document.getElementById('pickupError');
    const deliveryError = document.getElementById('deliveryError');
    const submitButton = document.getElementById('book_delivery');

    if (pickupPlace && deliveryPlace) {
      // Both addresses are valid, clear error messages and enable the submit button
      pickupError.textContent = '';
      deliveryError.textContent = '';
      submitButton.removeAttribute('disabled');
    } else {
      pickupError.textContent = !pickupPlace ? 'Enter a valid pickup address' : '';
      deliveryError.textContent = !deliveryPlace ? 'Enter a valid delivery address' : '';
      submitButton.setAttribute('disabled', 'true');
    }
  }
}

$(() => {
  const setPickupTimeCheckbox = $('#set_pickup_time');
  const pickupTimeLabel = $('#pickup-time');
  const pickupTimeField = $('#pickup_time');

  // Initially, check if the checkbox is checked and adjust the field
  pickupTimeField.prop('disabled', !setPickupTimeCheckbox.is(':checked'));
  pickupTimeLabel.hide();

  // Update the field's status when the checkbox changes
  setPickupTimeCheckbox.on('change', (e) => {
    pickupTimeField.prop('disabled', !$(e.target).is(':checked'));
    $(e.target).is(':checked') ? pickupTimeLabel.show() : pickupTimeLabel.hide();
  });
});
