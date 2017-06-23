from django.contrib import admin

# Register your models here.


from .models import Batches


class BatchesAdmin(admin.ModelAdmin):
    list_display = ('course', 'center', 'start_date', 'start_time', 'end_time', 'active')


admin.site.register(Batches, BatchesAdmin)
