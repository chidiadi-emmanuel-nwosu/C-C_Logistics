$(() => {
  console.log('helloooo');
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
    console.log('hello');
  });
});
