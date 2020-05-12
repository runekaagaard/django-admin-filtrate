from django.contrib import admin
from test_app.models import Case, Client
from test_app.models import CaseClientDateRangeFilter


class CaseAdmin(admin.ModelAdmin):
	list_filter = [('client', CaseClientDateRangeFilter)]

	class Media(): 
		pass
	
	def lookup_allowed(self, key, *args, **kwargs):
		if 'client__start_date' in key:
			return True
		else:
			return super(CaseAdmin, self).lookup_allowed(key, *args, **kwargs)
		
class ClientAdmin(admin.ModelAdmin):
	pass

admin.site.register(Case, CaseAdmin)
admin.site.register(Client, ClientAdmin)