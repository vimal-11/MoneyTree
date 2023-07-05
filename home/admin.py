from django.contrib import admin
from home.models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_filter = ['name']
    list_display = ['name', 'email', 'subject', 'contact_no']
    search_fields = ['name', 'email', 'subject']

    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)
