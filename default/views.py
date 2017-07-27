from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.


class DefaultPage(TemplateView):
    template_name = 'default/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'page_title': 'Home page'
        })
