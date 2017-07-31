from django.conf.urls import url

from . import views

app_name = 'contactus'

urlpatterns = [
    url(r'^$', views.ContactUsPage.as_view(), name='contactus'),
]