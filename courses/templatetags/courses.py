from django import template
from courses.models import Courses

register = template.Library()


@register.simple_tag
def courses():
    return Courses.objects.filter(active=True)


