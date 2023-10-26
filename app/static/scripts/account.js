$(() => {
  $('#editButton').click(function () {
    const addressElement = $('#user_address');
    const phoneElement = $('#user_phone');

    if ($(this).text() === 'Edit') {
      $(this).text('Save');
      addressElement.replaceWith(`
          <input
          type="text"
          class="block w-fit mb-2 p-1 rounded border bg-gray-100"
          id="update_address"
          value="${addressElement.text()}"
          placeholder="update your address">`
      );
      phoneElement.replaceWith(`
          <input
          type="text"
          class="block w-fit p-1 rounded border bg-gray-100"
          id="update_phone_number"
          value="${phoneElement.text()}">`
      );
    } else {
      $(this).text('Edit');
      const newAddress = $('#update_address').val();
      const newPhone = $('#update_phone_number').val();
      $('#update_address').replaceWith(`<p id="user_address">${newAddress}</p>`);
      $('#update_phone_number').replaceWith(`<p id="user_phone">${newPhone}</p>`);

      // Send updated data to the server using AJAX
      $.post('/dashboard/account/edit', { address: newAddress, phone_number: newPhone }, (data) => {
        $.get(data);
        // if (data.success) {
        //   // Show a success message
        //   alert('Profile updated successfully!');
        // } else {
        //   // Show an error message
        //   alert('Failed to update profile. Please try again.');
        // }
      });
    }
  });
});
