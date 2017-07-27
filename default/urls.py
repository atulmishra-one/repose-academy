from django.conf.urls import url

from . import views

app_name = 'default'

urlpatterns = [
    url(r'^$', views.DefaultPage.as_view(), name='default'),
]