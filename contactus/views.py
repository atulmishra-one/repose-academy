from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.mail import EmailMessage
# Create your views here.


class ContactUsPage(TemplateView):
    template_name = 'contactus/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {
        })

    def post(self, request, *args, **kwargs):
        name, phone, email, message = request.POST['name-id'], request.POST['phone-id'], request.POST['email-id'], \
                                      request.POST['message']

        html = """<table width="80%" style="border:1px solid #CCC; padding:10px;margin-top:20px;">
          <tr style="font-size:18px;">
            <td style="border-bottom:1px solid; padding:10px;">{0}</td>
            <td style="border-bottom:1px solid; padding:10px;">{1}</td>
            <td style="border-bottom:1px solid; padding:10px;">{2}</td>
          </tr>
          <tr>
            <td colspan="3" style="padding:12px;">{3}</td>
          </tr>
        </table>""".format(
            name,
            phone,
            email,
            message
        )

        email = EmailMessage("Repose coaching Message", html, "info@reposecoachingcenter.com", [
            'atulmishra.one@gmail.com'
        ])
        email.content_subtype = 'html'

        callback = email.send()

        if callback:
            message = 'Thank you for contacting us. Your message has been sent successfully.'
        else:
            message = 'Sorry, there was an error processing your message. Please later.'

        return render(request, self.template_name, {
            'message': message
        })