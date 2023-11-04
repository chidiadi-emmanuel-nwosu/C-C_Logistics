$(() => {
  console.log('hello');
  const acceptBtn = $('.accept_delivery');
  acceptBtn.click((e) => {
    const delivery = $(e.target).closest('.delivery');
    const deliveryId = delivery.find('.accept_delivery').data('delivery-id');
    $.ajax({
      type: 'POST',
      url: '/dashboard/accept-delivery',
      data: { delivery_id: deliveryId },
      success: (response) => {
        console.log(response);
        location.reload();
      },
      error: (error) => {
        alert('Error accepting the delivery.');
      }
    });
  });

  $('.toggle_delivery_details').click((e) => {
    const card = $(e.target).closest('.delivery').find('.additional_delivery_details');
    const toggleBtn = $(e.target).closest('.delivery').find('.toggle_delivery_details');
    card.toggleClass('hidden block');
    toggleBtn.toggleClass('fa-eye fa-eye-slash');
  });
});