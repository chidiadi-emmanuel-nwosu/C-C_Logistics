$(() => {
  $reg_type = $('#register_as');
  $agent_fields = $('#agent_fields');
  $agent_fields.hide();

  $reg_type.on('change', () => {
    if ($reg_type.val() === 'user') {
      $('#register_form_header').text('Register a user account');
      $('#drivers_license_number').removeAttr('required');
      $('#license_expiration_date').removeAttr('required');
      $('#license_image_file').removeAttr('required');
      $agent_fields.hide();
    } else {
      $('#register_form_header').text('Register a delivery agent account');
      $agent_fields.show();
      $('#drivers_license_number').attr('required', 'required');
      $('#license_expiration_date').attr('required', 'required');
      $('#license_image_file').attr('required', 'required');
    }
  });
});
