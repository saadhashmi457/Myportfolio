from django.contrib import admin
from contacts.models import contact_model

# Register your models here.
class contact_admin(admin.ModelAdmin):
    list_display=('Name','Email','Message')
    
admin.site.register(contact_model,contact_admin)
