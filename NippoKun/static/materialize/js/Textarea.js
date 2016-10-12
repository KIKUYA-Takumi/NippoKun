$(document).ready(function() {
    Materialize.updateTextFields();
    $('select').material_select();
  });
$('#textarea1').val('New Text');
$('#textarea1').trigger('autoresize');