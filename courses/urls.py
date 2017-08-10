from django.conf.urls import url

from . import views

app_name = 'courses'

urlpatterns = [
    url(r'^(?P<slug>[-\w]+)/$', views.CourseDetail.as_view(), name='detail'),
]