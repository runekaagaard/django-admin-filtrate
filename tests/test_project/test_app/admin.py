from django.contrib import admin
from test_app.models import Case

class CaseAdmin(admin.ModelAdmin):
	list_filter = ['start_date']

	class Media():
		js = ()
		css = {}

admin.site.register(Case, CaseAdmin)