from django.contrib import admin
from test_app.models import Case, Client

class CaseAdmin(admin.ModelAdmin):
	list_filter = ['client']

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