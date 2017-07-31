from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class ContactUsPage(TemplateView):
    template_name = 'contactus/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
            'page_title': 'Home page'
        })