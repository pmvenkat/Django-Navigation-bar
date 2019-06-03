from django.urls import path
from .views import MainPageView, ContactPageView, DocumentationPageView

app_name = 'navbar'

urlpatterns = [
    path('', MainPageView.as_view(), name='mainpage'),
    path('contactus/', ContactPageView.as_view(), name='contactus'),
    path('documentation/', DocumentationPageView.as_view(), name='documentation'),
]