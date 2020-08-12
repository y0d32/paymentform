""" This is the admin module """

from django.contrib import admin
from django.urls import path
from . import views # pylint:disable=relative-beyond-top-level
from .models import Card # pylint:disable=relative-beyond-top-level


urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.process_payment, name='process_payment')
]


class CardAdmin(admin.ModelAdmin):
    """ This is the  modelel Admin """
    date_hierarchy = 'created'
    list_display = (
        'creditcard_number',
        'card_holder',
        'security_code',
        'amount',
        'expiration_date',
        'expiration_date'
        )


admin.site.register(Card)
