from django.conf.urls import url

from . import views

app_name = 'branches'

urlpatterns = [
    url(r'^$', views.BranchView.as_view(), name='branches'),
]