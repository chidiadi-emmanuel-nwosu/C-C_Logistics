$(() => {
  // Function to fetch and display pending deliveries
  const fetchAllDeliveries = () => {
    displayDeliveries(myDeliveries);
  };

  const fetchPendingDeliveries = () => {
    displayDeliveries(myDeliveries.filter((e) => e.order_status !== 'Delivered'));
  };

  // Function to fetch and display fulfilled deliveries
  function fetchFulfilledDeliveries () {
    displayDeliveries(myDeliveries.filter((e) => e.order_status === 'Delivered'));
  }

  // Function to fetch and display deliveries as cards
  function displayDeliveries (deliveries) {
    const deliveryCards = $('#delivery-cards');
    deliveryCards.empty();

    if (deliveries.length === 0) {
      deliveryCards.append('<p class="text-center text-gray-500">No deliveries found.</p>');
      return;
    }

    $.each(deliveries, function (index, delivery) {
      const cardHtml = `
            <div class="delivery border border-gray-300 shadow rounded p-4 h-fit">
                <h2 class="font-medium text-base mb-2">From: ${delivery.pickup_address}</h2>
                <p class="text-gray-600 text-sm mb-2">To: ${delivery.delivery_address}</p>
                     ${currentUser === 'User'
                ? `<p class="text-gray-600 text-sm mb-2">Delivery Agent: ${delivery.agent ? delivery.agent.first_name : ''} ${delivery.agent ? delivery.agent.last_name : ''}</p> `
: `<p class="text-gray-600 text-sm mb-2">Parcel Owner: ${delivery.user.first_name} ${delivery.user.last_name}</p> `}
                <p class="text-gray-600 text-sm mb-2">Status: ${delivery.order_status}</p>
                <div class="additional_delivery_details hidden mt-2">
                    <p class="text-gray-600 text-sm mb-2">Contact person: ${delivery.contact_person}</p>
                    <p class="text-gray-600 text-sm mb-2">Contact phone number: ${delivery.contact_phone_number}</p>
                    <p class="text-gray-600 text-sm mb-2">Delivery Instructions: ${delivery.delivery_instruction}</p>
                    <p class="text-gray-600 text-sm mb-2">Estimated distance: ${delivery.estimated_distance}</p>
                    <p class="text-gray-600 text-sm mb-2">Estimated duration: ${delivery.estimated_duration}</p>
                    <p class="text-gray-600 text-sm mb-2">Delivery cost: ${delivery.delivery_cost}</p>
                </div>
                <div class="flex space-x-4">
                     ${currentUser === 'User' && delivery.order_status !== 'Delivered'
                    ? `<button class='track_delivery bg-orange-500 text-white px-2 py-1 rounded-md mt-2 track-button' data-delivery-id='${delivery.id}'>Track</button>`
: currentUser === 'DeliveryAgent' && delivery.order_status !== 'Delivered' ? `<button class='delivered bg-orange-500 text-white px-2 py-1 rounded-md mt-2 track-button' data-delivery-id='${delivery.id}'>Parcel delivered</button>` : ''
}
                    ${delivery.order_status === 'pending'
                    ? `<button class="delete_delivery text-red-500 px-2 py-1 rounded-md mt-2 underline underline-offset-2" data-delivery-id="${delivery.id}">Delete</button>`
: ''}
                </div>
                <div class="flex justify-end mt-2">
                    <i class="fa-solid fa-eye cursor-pointer toggle_delivery_details"></i>
                </div>
            </div>
        `;
      deliveryCards.append(cardHtml);
    });

    $('.toggle_delivery_details').click((e) => {
      const card = $(e.target).closest('.delivery').find('.additional_delivery_details');
      const toggleBtn = $(e.target).closest('.delivery').find('.toggle_delivery_details');
      card.toggleClass('hidden block');
      toggleBtn.toggleClass('fa-eye fa-eye-slash');
    });

    $('.delete_delivery').click((e) => {
      const delivery = $(e.target).closest('.delivery');
      const deliveryId = delivery.find('.delete_delivery').data('delivery-id');

      $('#custom-confirm-popup').show();

      $('#confirm-yes').click(() => {
        $.ajax({
          type: 'POST',
          url: '/delete_delivery',
          data: { delivery_id: deliveryId },
          success: (response) => {
            delivery.remove();
            $('#custom-confirm-popup').hide();
          },
          error: (error) => {
            $('#custom-confirm-popup').hide();
            alert('Error deleting the delivery.');
          }
        });
      });

      $('#confirm-no').click(() => $('#custom-confirm-popup').hide());
    });
  }

  // Load all deliveries by default
  fetchAllDeliveries();

  $('#custom-confirm-popup').hide();
  // Add click event handlers for filter buttons
  $('#show-all').click(fetchAllDeliveries);

  $('#show-pending').click(fetchPendingDeliveries);

  $('#show-fulfilled').click(fetchFulfilledDeliveries);
});
