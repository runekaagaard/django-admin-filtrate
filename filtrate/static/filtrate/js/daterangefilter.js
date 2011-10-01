(function(jQuery, that) {
  jQuery(function() {
    if (!filtrate.is_active() || typeof that.filtrate.language_code === 'undefined') return;
    // The default language code for english should be a blank string
    if (that.filtrate.language_code === 'en') {
      language_code = '';
    };
    var regional = jQuery.datepicker.regional[language_code];
    regional['dateFormat'] = 'yy-mm-dd'
    jQuery('input.filtrate_date').datepicker(regional);
    jQuery('input.filtrate_date').each(function() {
      var id = jQuery(this).attr('id').replace('__alt', '');
      jQuery(this).datepicker("option", "altField", "#" + id);
      jQuery(this).datepicker("option", "altFormat", 'yy-mm-dd');
    });
    jQuery('form.filtrate_daterange_form input[type=submit]').click(function() {
      jQuery(this).parent().find('.filtrate_date').attr('disabled', 'disabled');
    });
  });
})(jQuery || django.jQuery, this);