from django.shortcuts import render
from django.views.generic import TemplateView
from courses.models import Courses
from django.core.mail import EmailMessage
from cms.models import Cms

# Create your views here.


class DefaultPage(TemplateView):
    template_name = 'default/index.html'
        # course_id = request.POST['cat2']
        # name = request.POST['yourname']
        # email = request.POST['email-id']
        # phone = request.POST['phone']
        #
        # course = Courses.objects.get(pk=course_id)
        #
        # html = """
        # <table style='padding: 10px; border-bottom: 2px solid #CCC;'>
        # <tr><td style='border-bottom: 1px solid #CCC;'><h2 style='margin-bottom:3px'>Course Enquiry</h2></td></tr>
        # <tr><td style='padding:10px;'>Contact detail
        #     <table style='padding:10px;'>
        #     <td>{0}</td><td>{1}</td><td>{2}</td>
        #     </table>
        # </td></tr>
        # <tr><td>Course Interested: {3}</td></tr>
        # </table>
        # """.format(name, phone, email, course.name)
        #
        # email = EmailMessage("Repose New Enquiry", html, "info@reposecoachingcenter.com", [
        #     'reposeaksingh1234@gmail.com'
        # ])
        # email.content_subtype = 'html'
        #
        # callback = False
        #
        # error = None
        # success = None
        #
        # if callback:
        #     success = 'Thank you for contacting us. Your message has been sent successfully.'
        # else:
        #     error = 'Sorry, there was an error processing your message. Please later.'
        #
        # return render(request, self.template_name, {
        #     'success': success,
        #     'error': error
        # })
