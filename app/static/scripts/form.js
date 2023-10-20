$(() => {
  $reg_type = $('#register_as');
  $agent_fields = $('#agent_fields');
  $agent_fields.hide();
  $('#register_form_header').removeClass('mt-16');

  $reg_type.on('change', () => {
    if ($reg_type.val() === 'user') {
      $('#register_form_header').removeClass('mt-16');
      $('#register_form_header').text('Register a user account');
      $('#drivers_license_number').removeAttr('required');
      $('#license_expiration_date').removeAttr('required');
      $('#license_image_file').removeAttr('required');
      $agent_fields.hide();
    } else {
      $('#register_form_header').addClass('mt-16');
      $('#register_form_header').text('Register a delivery agent account');
      $agent_fields.show();
      $('#drivers_license_number').attr('required', 'required');
      $('#license_expiration_date').attr('required', 'required');
      $('#license_image_file').attr('required', 'required');
    }
  });
});

$(() => {
  const category = $('.flash-message').data('id');
  const categoryClasses = {
    success: 'bg-green-100 border-green-500 text-green-700',
    info: 'bg-blue-100 border-blue-500 text-blue-700',
    warning: 'bg-yellow-100 border-yellow-500 text-yellow-700',
    danger: 'bg-red-100 border-red-500 text-red-700'
  };
  $('.flash-message').addClass(categoryClasses[category]).show();

  setTimeout(function () {
    $('.flash-message').hide();
  }, 5000);

  $('.datepicker').datepicker({
    dateFormat: 'dd/mm/yy' // Set the desired date format
  });
});

// dashboard form

$(() => {
  const setPickupTimeCheckbox = $('#set-pickup-time');
  const pickupTimeLabel = $('#pickup_time');
  const pickupTimeField = $('#pickup-time');

  // Initially, check if the checkbox is checked and adjust the field
  pickupTimeField.prop('disabled', !setPickupTimeCheckbox.is(':checked'));
  pickupTimeLabel.hide();

  // Update the field's status when the checkbox changes
  setPickupTimeCheckbox.on('change', (e) => {
    pickupTimeField.prop('disabled', !$(e.target).is(':checked'));
    $(e.target).is(':checked') ? pickupTimeLabel.show() : pickupTimeLabel.hide();
  });
});
