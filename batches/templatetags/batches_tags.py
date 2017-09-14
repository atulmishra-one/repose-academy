from django import template
from django.template.defaultfilters import stringfilter
from batches.models import Batches

import datetime

register = template.Library()


@register.inclusion_tag('batches/home_widget.html')
def home_page_batches_widget():
    latest_batches = Batches.objects.filter(active=True, show_on_home_page=True).all()[0:3]
    return dict(
        latest_batches=latest_batches
    )


@register.simple_tag
def format_batch_date(value, arg):
    return value.strftime(arg)
