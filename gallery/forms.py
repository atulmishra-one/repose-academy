# -*- coding: utf-8 -*-
# Copyright (c) Zbigniew Siciarz 2012-2016.

from __future__ import unicode_literals

from django import forms

from .models import Photo


class PhotoForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = ['title', 'image']
