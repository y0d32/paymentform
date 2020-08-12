""" This is the models file """
from django.db import models


class Card(models.Model):
    """ This is the class models """
    creditcard_number = models.CharField(max_length=16, blank=False, null=False)
    card_holder = models.CharField(max_length=30, blank=False, null=False)
    security_code = models.CharField(max_length=3, blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateTimeField()

    def __str__(self):
        return 'MyModel: {}'.format(self.card_holder)
      