from django import template
from cms.models import Cms
from cms.models import News
from cms.models import SelectedStudent
from cms.models import StudentTestimonial


register = template.Library()


@register.simple_tag
def about_us():
    return Cms.objects.get(name='main-page-about-us').content


@register.simple_tag
def director_message():
    return Cms.objects.get(name='director-message-main').content


@register.inclusion_tag('cms/news_widget.html')
def latest_news():
    news = News.objects.all()[0:3]
    return dict(
        latest_news=news
    )


@register.inclusion_tag('cms/selected_student_widget.html')
def selected_students():
    students = SelectedStudent.objects.all()[0:3]
    return dict(
        selected_students=students
    )


@register.inclusion_tag('cms/success_stories_widget.html')
def success_stories():
    stories = StudentTestimonial.objects.all()[0:5]
    return dict(
        success_stories=stories
    )
