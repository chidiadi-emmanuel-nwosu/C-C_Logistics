$(() => {
  $('.menu-toggle').removeClass('hidden');
  $('.nav-bar').removeClass('hidden');
});

$(() => {
  $('#return-btn').on('click', (event) => {
    event.preventDefault();

    $('html, body').animate({ scrollTop: 0 }, 800);
  });
});
