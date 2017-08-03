from django.contrib import admin
from django.forms import ModelForm
from django.contrib.admin import ModelAdmin
from suit_redactor.widgets import RedactorWidget

# Register your models here.


from .models import Courses

# class EditorForm(ModelForm):
#     class Meta:
#
#         widgets = {
#             'description': RedactorWidget(editor_options={
#
#                 'lang': 'en','buttons': ['html', '|', 'formatting', '|', 'bold', 'italic']}),
#
#             'syllabus': RedactorWidget(editor_options={
#
#                 'lang': 'en','buttons': ['html', '|', 'formatting', '|', 'bold', 'italic']}),
#         }
#
# class EditorAdmin(ModelAdmin):
#     model = Courses
#     form = EditorForm
#
#
#     fields = ['name', 'active', 'slug','description','syllabus']
#
#
# admin.site.register(Courses, EditorAdmin)
# admin.register(Courses,EditorForm)

class EditorForm(ModelForm):
    class Meta:
        widgets = {
            'description': RedactorWidget(editor_options={'lang': 'en'}),
            'syllabus': RedactorWidget(editor_options={'lang': 'en'})
        }


class EditorAdmin(ModelAdmin):
    model = Courses
    form = EditorForm

    fields = ['name', 'active', 'slug','description','syllabus']


admin.site.register(Courses, EditorAdmin)


# admin.site.register(Courses, EditorAdmin)


