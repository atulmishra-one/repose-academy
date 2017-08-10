from django.shortcuts import render
from django.views.generic import DetailView
from courses.models import Courses

# Create your views here.


class CourseDetail(DetailView):
    template_name = 'courses/single.html'
    model = Courses
