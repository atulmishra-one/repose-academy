from django.conf.urls import url

from . import views

app_name = 'batches'

urlpatterns = [
    url(r'^', views.BatchesListView.as_view(), name='list'),
]