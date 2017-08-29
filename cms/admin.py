from django.contrib import admin
from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from suit_redactor.widgets import RedactorWidget

# Register your models here.


from .models import Cms


class EditorForm(ModelForm):
    class Meta:
        widgets = {
            'content': RedactorWidget(editor_options={'lang': 'en'})
        }


class EditorAdmin(ModelAdmin):
    model = Cms
    form = EditorForm

    fields = ['name', 'content']


admin.site.register(Cms, EditorAdmin)




