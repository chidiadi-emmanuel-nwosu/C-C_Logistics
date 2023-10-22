// $(() => {
// // Function to fetch and display pending deliveries
//   // function fetchPendingDeliveries () {
//   //   $.ajax({
//   //     url: '/get_pending_deliveries',
//   //     method: 'GET',
//   //     success: function (data) {
//   //       displayDeliveries(data);
//   //     }
//   //   });
//   // }

//   // Function to fetch and display fulfilled deliveries
//   // function fetchFulfilledDeliveries () {
//   //   $.ajax({
//   //     url: '/get_fulfilled_deliveries',
//   //     method: 'GET',
//   //     success: function (data) {
//   //       displayDeliveries(data);
//   //     }
//   //   });
//   // }

//   // Function to fetch and display deliveries as cards
//   function displayDeliveries (deliveries) {
//     const deliveryCards = $('#delivery-cards');
//     deliveryCards.empty();

//     if (deliveries.length === 0) {
//       deliveryCards.append('<p class="text-center text-gray-500">No deliveries found.</p>');
//       return;
//     }

//     $.each(deliveries, function (index, delivery) {
//       const cardHtml = `
//             <div class="border border-gray-300 shadow rounded p-4">
//                 <h2 class="font-medium text-base">From: ${delivery.pickup_address}</h2>
//                 <p class="text-gray-600 text-sm">To: ${delivery.delivery_address}</p>
//                 <p class="text-gray-600 text-sm">Stattus: ${delivery.status}</p>
//                 <button class="bg-orange-500 text-white px-2 py-1 rounded-md mt-2 track-button" data-order-id="${delivery.order_id}">Track</button>
//             </div>
//         `;
//       deliveryCards.append(cardHtml);
//     });
//   }

//   // Load pending deliveries by default
//   fetchPendingDeliveries();

//   // Add click event handlers for filter buttons
//   $('#pending-btn').click(function () {
//     fetchPendingDeliveries();
//   });

//   $('#fulfilled-btn').click(function () {
//     fetchFulfilledDeliveries();
//   });
// });
