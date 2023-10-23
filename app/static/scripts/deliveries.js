$(() => {
// Function to fetch and display pending deliveries
  const fetchAllDeliveries = () => {
    displayDeliveries(myDeliveries);
  };

  const fetchPendingDeliveries = () => {
    displayDeliveries(myDeliveries.filter((e) => e.order_status === 'pending'));
  };

  // Function to fetch and display fulfilled deliveries
  function fetchFulfilledDeliveries () {
    displayDeliveries(myDeliveries.filter((e) => e.order_status === 'completed'));
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
                <p class="text-gray-600 text-sm mb-2">Delivery Agent: ${delivery.agent}</p>
                <p class="text-gray-600 text-sm mb-2">Status: ${delivery.order_status}</p>
                <div class="additional_delivery_details hidden mt-2">
                    <p class="text-gray-600 text-sm mb-2">Contact person: ${delivery.contact_person}</p>
                    <p class="text-gray-600 text-sm mb-2">Contact phone number: ${delivery.contact_phone_number}</p>
                    <p class="text-gray-600 text-sm mb-2">Delivery Instructions: ${delivery.delivery_instruction}</p>
                    <p class="text-gray-600 text-sm mb-2">Estimated distance: ${delivery.estimated_distance}</p>
                    <p class="text-gray-600 text-sm mb-2">Estimated duration: ${delivery.estimated_duration}</p>
                    <p class="text-gray-600 text-sm mb-2">Delivery cost: ${delivery.delivery_cost}</p>
                </div>
                <button class="bg-orange-500 text-white px-2 py-1 rounded-md mt-2 track-button" data-order-id="${delivery.order_id}">Track</button>
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
  }

  // Load all deliveries by default
  fetchAllDeliveries();

  // Add click event handlers for filter buttons
  $('#show-all').click(fetchAllDeliveries);

  $('#show-pending').click(fetchPendingDeliveries);

  $('#show-fulfilled').click(fetchFulfilledDeliveries);
});
