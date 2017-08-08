from django.contrib import admin
from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from suit_redactor.widgets import RedactorWidget

# Register your models here.


from .models import Courses


class EditorForm(ModelForm):
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'en'})
        }


class EditorAdmin(ModelAdmin):
    model = Courses
    form = EditorForm

    fields = ['name', 'active', 'slug', 'description']


admin.site.register(Courses, EditorAdmin)



