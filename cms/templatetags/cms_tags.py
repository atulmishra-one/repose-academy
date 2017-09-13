from django import template
from cms.models import Cms


register = template.Library()


@register.simple_tag
def about_us():
    return Cms.objects.get(name='main-page-about-us').content


@register.simple_tag
def director_message():
    return Cms.objects.get(name='director-message-main').content
