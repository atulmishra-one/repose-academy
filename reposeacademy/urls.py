"""reposeacademy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls import include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from django.conf.urls.static import static
from cms.views import about_us
from reposeforms.views import CourseEnquiryView, ThankYouView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^gallery/', include('gallery.urls', namespace='gallery')),
    url(r'^', include('default.urls', namespace='default')),
    url(r'^contactus/', include('contactus.urls')),
    url(r'^courses/', include('courses.urls', namespace='courses')),
    url(r'^branches/', include('branches.urls', namespace='branches')),
    url(r'^about_us/', about_us),
    url(r'^batches/', include('batches.urls', namespace='batches')),
    url(r'^course_enquiry/', CourseEnquiryView.as_view(), name='course_enquiry'),
    url(r'^thanks/',ThankYouView.as_view())

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
