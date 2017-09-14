from django.shortcuts import render
from django.views.generic import ListView
from batches.models import Batches

# Create your views here.


class BatchesListView(ListView):
    template_name = 'batches/list.html'
    model = Batches
