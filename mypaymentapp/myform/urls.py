""" This is the url file """
from django.urls import path
from . import views #pylint:disable=relative-beyond-top-level


urlpatterns = [
    path('', views.process_payment, name='process_payment'),
    path('thanks', views.index, name='index'),
]
