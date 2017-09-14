from django.contrib import admin
from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from suit_redactor.widgets import RedactorWidget

# Register your models here.


from .models import Cms
from .models import News
from .models import SelectedStudent
from .models import StudentTestimonial


class EditorForm(ModelForm):
    class Meta:
        widgets = {
            'content': RedactorWidget(editor_options={'lang': 'en'}),
            'description': RedactorWidget(editor_options={'lang': 'en'})
        }


class CmsEditorAdmin(ModelAdmin):
    model = Cms
    form = EditorForm
    fields = ['name', 'content']


class NewsEditorAdmin(ModelAdmin):
    model = News
    form = EditorForm
    fields = ['title', 'date_published', 'description']


class StudentTestimonialEditorAdmin(ModelAdmin):
    model = StudentTestimonial
    form = EditorForm
    fields = ['name', 'content']


class SelectedStudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'details', )

admin.site.register(Cms, CmsEditorAdmin)
admin.site.register(News, NewsEditorAdmin)
admin.site.register(SelectedStudent, SelectedStudentAdmin)
admin.site.register(StudentTestimonial, StudentTestimonialEditorAdmin)




