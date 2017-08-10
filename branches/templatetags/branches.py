from django import template
from branches.models import Branches

register = template.Library()


@register.simple_tag
def get_main_branch():
    return Branches.objects.filter(is_main_branch=True, active=True)[0]


