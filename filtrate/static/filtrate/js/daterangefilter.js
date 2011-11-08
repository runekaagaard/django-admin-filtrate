(function($, that) { $(function() {
	if (!filtrate.is_active() 
	    || typeof that.filtrate.datepicker_region === 'undefined') return;
	
	var regional = $.datepicker.regional[that.filtrate.datepicker_region];
	regional['dateFormat'] = that.filtrate.datepicker_date_format;
	
	$('input.filtrate_date_hidden').each(function() {
		var datepicker = $('#' + $(this).attr('id') + '__alt');
		regional['altField'] = $(this);
		regional['altFormat'] = 'yy-mm-dd';
		datepicker.datepicker(regional);
		
		// One would expect datepicker to update the alternate field 
		// automatically, but apparently it doesn't. It's probably me missing
		// something. Update it manually instead.
		if (datepicker.val() !== "") {
			var parts = datepicker.val().split('-');
			datepicker.datepicker("setDate", new Date (Number(parts[0]), 
													   Number(parts[1]-1), 
				                                       Number(parts[2])));
		}
	});
	
	/**
	 * When the submit button is clicked, we disable all the __alt fields so
	 * they wont get submitted. We also disable fields whose alt __alt fields
	 * are empty.
	 */
	$('form.filtrate_daterange_form input[type=submit]').click(function() {
		$(this).parent().find('.filtrate_date_hidden').each(function() {
			var datepicker = $('#' + $(this).attr('id') + '__alt');
			if (datepicker.val() === "") {
				$(this).attr('disabled', 'disabled');	
			}
			datepicker.attr('disabled', 'disabled');
		});
	});
	
});})(jQuery || django.jQuery, this);