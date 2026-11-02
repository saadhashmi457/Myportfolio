from django.contrib import admin
from Services.models import services_model

# Register your models here.

class services_admin(admin.ModelAdmin):
    list_display=('Service_title','Service_detail')
    
admin.site.register(services_model,services_admin)
