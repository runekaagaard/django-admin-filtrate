from django.conf import settings

FILTRATE = {
	# See http://jqueryui.com/demos/datepicker/#localization.
	'datepicker_region': 'en-GB',
	# See http://docs.jquery.com/UI/Datepicker/formatDate.
	'datepicker_date_format': 'yy-mm-dd',
}

try:
	FILTRATE.update(settings.FILTRATE)
except AttributeError:
	pass