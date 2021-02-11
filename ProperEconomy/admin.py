from django.contrib import admin

# Register your models here.
from .models import ClientInfo
class ClientInfoAdmin(admin.ModelAdmin):
    model = ClientInfo
    list_display = ('name', 'phone',)
admin.site.register(ClientInfo, ClientInfoAdmin)