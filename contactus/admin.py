from django.contrib import admin

# Register your models here.

from .models import ContactUs


class ContactUsAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False


admin.site.register(ContactUs, ContactUsAdmin)
