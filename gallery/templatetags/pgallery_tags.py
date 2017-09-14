# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2012-2016.

from __future__ import unicode_literals

from django import template

from gallery.models import Gallery, Photo

register = template.Library()


@register.inclusion_tag('gallery/box.html')
def get_recent_galleries():
    """
    Returns most recent galleries.
    """
    selected_student = Gallery.objects.published()[0]
    photos = Photo.objects.filter(gallery=selected_student.pk)[:6]
    return dict(
            photos=photos
    )



# @register.simple_tag
# def get_recent_galleries(count=3):
#     """
#     Returns most recent galleries.
#     """
#     return Gallery.objects.published().order_by('-shot_date')[:count]


# @register.simple_tag
# def get_gallery_archive_dates():
#     """
#     Returns datetime objects for all months in which galleries were added.
#     """
#     return Gallery.objects.published().dates('shot_date', 'month', order='DESC')
#
#
# @register.simple_tag
# def get_popular_tags(count=10):
#     """
#     Returns most popular tags.
#     """
#     return Photo.objects.popular_tags(count)
