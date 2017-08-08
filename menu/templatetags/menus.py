from django import template
from courses.models import Courses

register = template.Library()


@register.inclusion_tag('menu/top_menu.html')
def get_menus():
    courses = Courses.objects.all()
    return dict(
        courses=courses
    )
