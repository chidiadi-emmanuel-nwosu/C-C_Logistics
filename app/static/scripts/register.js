$(() => {
  const $register_toggle = $('.register_toggle');
  const $register_btn = $('.register_toggle_btn');
  $register_toggle.on('click', () => {
    $register_btn.toggleClass('translate-x-0 translate-x-full');

    if ($register_btn.hasClass('translate-x-0')) {
      $register_btn.text('User');
      $('#register').attr('href', '/register/user');
    } else {
      $register_btn.text('Rider');
      $('#register').attr('href', '/register/rider');
    }
    console.log('hello');
  });
});
