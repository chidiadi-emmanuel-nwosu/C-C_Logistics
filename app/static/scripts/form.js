
$(() => {
  const category = $('.flash-message').data('id');
  const categoryClasses = {
    success: 'bg-green-100 border-green-500 text-green-700',
    info: 'bg-blue-100 border-blue-500 text-blue-700',
    warning: 'bg-yellow-100 border-yellow-500 text-yellow-700',
    danger: 'bg-red-100 border-red-500 text-red-700'
  };
  $('.flash-message').addClass(categoryClasses[category]).show();

  setTimeout(function () {
    $('.flash-message').hide();
  }, 5000);

  $('.datepicker').datepicker({
    dateFormat: 'dd/mm/yy' // Set the desired date format
  });
});

// dashboard form
