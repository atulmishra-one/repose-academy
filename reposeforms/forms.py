from django import forms
from courses.models import Courses
from django.core.mail import EmailMessage


class CourseEnquiryForm(forms.Form):
    course = forms.IntegerField(required=True)
    full_name = forms.CharField(min_length=2, max_length=255, required=True)
    email_address = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=12, min_length=2, required=True)

    def send_mail(self):
        course = self.cleaned_data['course']
        full_name = self.cleaned_data['full_name']
        email_address = self.cleaned_data['email_address']
        phone_number = self.cleaned_data['phone_number']

        course = Courses.objects.get(pk=course)

        html = """
        <table style='padding: 10px; border-bottom: 2px solid #CCC;'>
        <tr><td style='border-bottom: 1px solid #CCC;'><h2 style='margin-bottom:3px'>Course Enquiry</h2></td></tr>
        <tr><td style='padding:10px;'>Contact detail
            <table style='padding:10px;'>
            <td>{0}</td><td>{1}</td><td>{2}</td>
            </table>
        </td></tr>
        <tr><td>Course Interested: {3}</td></tr>
        </table>
        """.format(full_name, phone_number, email_address, course.name)

        email = EmailMessage("Repose New Enquiry", html, "info@reposecoachingcenter.com", [
            #'reposeaksingh1234@gmail.com',
            'atulmishra.one@gmail.com'
        ])
        email.content_subtype = 'html'

        callback = email.send()
        return callback



