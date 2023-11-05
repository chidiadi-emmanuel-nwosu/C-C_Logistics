$(() => {
  const deliveredBtn = $('.delivered');
  deliveredBtn.click((e) => {
    const delivery = $(e.target).closest('.delivery');
    const deliveryId = delivery.find('.delivered').data('delivery-id');
    $.ajax({
      type: 'POST',
      url: '/dashboard/delivered',
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
});
