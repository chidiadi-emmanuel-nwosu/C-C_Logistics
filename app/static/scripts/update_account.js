$(() => {
  $agent_fields = $('#agent_fields');
  $agent_fields.hide();

  $reg_type.on('change', () => {
    if ($reg_type.val() === 'User') {
      $('#drivers_license_number').removeAttr('required');
      $('#license_expiration_date').removeAttr('required');
      $('#license_image_file').removeAttr('required');
      $agent_fields.hide();
    } else {
      $agent_fields.show();
      $('#drivers_license_number').attr('required', 'required');
      $('#license_expiration_date').attr('required', 'required');
      $('#license_image_file').attr('required', 'required');
    }
  });
});
