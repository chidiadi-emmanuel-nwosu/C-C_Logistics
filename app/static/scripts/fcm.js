$(() => {
  let subscription = null;

  // Replace 'YOUR_VAPID_PUBLIC_KEY' with your actual VAPID public key
  const applicationServerKey = 'BDnOafVJ6i8k2D3Z8bdEERIhihFtRdTaW6am86NbosgDc9t2fB18FPjZIYfcZd7rlXu2pHadT0BWbh68J8P7N4I';

  const getToken = async () => {
    try {
    // Check for service worker support in the browser
      if ('serviceWorker' in navigator) {
        const registration = await navigator.serviceWorker.register('/static/scripts/service-worker.js');

        subscription = await registration.pushManager.subscribe({
          userVisibleOnly: true,
          applicationServerKey
        });
        console.log(JSON.stringify(subscription));

      // Send the subscription to the server
      // $.ajax({
      //   type: 'POST',
      //   url: '/subscribe',
      //   contentType: 'application/json',
      //   data: JSON.stringify({
      //     user_id: 'user123', // Replace with the user's ID
      //     subscription: JSON.stringify(subscription)
      //   }),
      //   success: function () {
      //     console.log('Subscribed successfully.');
      //   },
      //   error: function (error) {
      //     console.error('Error subscribing:', error);
      //   }
      // });
      } else {
        console.error('Service workers not supported in this browser.');
      }
    } catch (error) {
      console.error('Error registering service worker:', error);
    }
  };
  getToken();
});
