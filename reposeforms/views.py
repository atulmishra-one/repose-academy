from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from .forms import CourseEnquiryForm


# Create your views here.


class CourseEnquiryView(FormView):
    form_class = CourseEnquiryForm
    template_name = 'reposeforms/course_enquiry.html'
    success_url = '/thanks/'

    def form_valid(self, form):
        form.send_mail()
        return super(CourseEnquiryView, self).form_valid(form)


class ThankYouView(TemplateView):
    template_name = 'reposeforms/course_success.html'
