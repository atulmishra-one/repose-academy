from django.shortcuts import render

# Create your views here.


def about_us(request):
    return render(request, 'cms/about_us.html')
