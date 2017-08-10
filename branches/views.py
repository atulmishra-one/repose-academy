from django.shortcuts import render

from django.views.generic import ListView
from branches.models import Branches

# Create your views here.


class BranchView(ListView):
    template_name = 'branches/list.html'
    model = Branches

    def get_queryset(self):
        return Branches.objects.filter(active=True)
