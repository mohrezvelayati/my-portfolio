from django.urls import path
from .views import *

app_name = 'main'


urlpatterns = [
    path('', index_view, name='index'),
    path('', contact_view, name='contact')
]
