$(() => {
  // Event handler to toggle menu
  $menu = $('.menu-toggle');
  $navBar = $('.nav-bar');
  $menu.on('click', () => {
    if ($menu.hasClass('active')) {
      $menu.removeClass('active');
      $navBar.css('display', 'none');
    } else {
      $menu.addClass('active');
      $navBar.css('display', 'flex');
    }
  });
});

$(() => {
  $('.actions a').on('click', (event) => {
    if (event.target.hash !== '') {
      event.preventDefault();
      const hash = event.target.hash;

      $('html, body').animate(
        {
          scrollTop: $(hash).offset().top
        },
        800,
        () => {
          window.location.hash = hash;
        }
      );
    }
  });
});
