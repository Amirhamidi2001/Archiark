from django.urls import path
from .views import *

app_name = 'website'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('project/', ProjectView.as_view(), name='project'),
    path('single/', SingleView.as_view(), name='single'),
    path('service/', ServiceView.as_view(), name='service'),
]
