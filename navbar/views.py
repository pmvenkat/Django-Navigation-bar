from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class MainPageView(TemplateView):
    template_name = 'navbar/mainpage.html'

class ContactPageView(TemplateView):
    template_name = 'navbar/contactus.html'

class DocumentationPageView(TemplateView):
    template_name = 'navbar/documentation.html'