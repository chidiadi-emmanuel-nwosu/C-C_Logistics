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
  const $accountBtn = $('#account-btn');
  const $accountDropdown = $('#account-dropdown');

  // Show/hide the dropdown menu on button click
  $accountBtn.on('click', (event) => {
    event.stopPropagation();
    console.log('dropdown');
    $accountDropdown.toggleClass('hidden');
  });

  // Hide the dropdown when clicking outside of it
  $(document).on('click', function (event) {
    if (!$accountDropdown.is(event.target) && $accountDropdown.has(event.target).length === 0) {
      $accountDropdown.addClass('hidden');
    }
  });
});
