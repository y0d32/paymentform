""" This is the forms file """
from datetime import date
from django.forms import ModelForm
from .models import Card  #pylint:disable=relative-beyond-top-level


class CardFormNew(ModelForm):
    """ This is the constructor """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['creditcard_number'].required = True #pylint:disable=trailing-whitespace
        self.fields['card_holder'].required = True
        self.fields['amount'].required = True
        self.fields['expiration_date'].required = True


    class Meta: #pylint:disable=too-few-public-methods
        """ Write the name of models for which the form is made """
        model = Card #pylint:disable=trailing-whitespace
        labels = { #pylint:disable=trailing-whitespace
            'creditcard_number':'Your Credit Card Number',
            'card_holder':'Name of the Owner of the Card',
            'security_code':'CVC Security Code',
            'amount':'The Amount you want to transfer',
            'expiration_date':'Expiration Date'}
        fields = ["creditcard_number", "card_holder", "security_code", "amount", "expiration_date"]


    def clean(self):
        """ This function will be used for the validation
            Data from the form is fetched using super function"""
        super(CardFormNew, self).clean()
        # extract the username and text field from the data
        creditcard_number = self.cleaned_data.get('creditcard_number')
        card_holder = self.cleaned_data.get('card_holder')
        security_code = self.cleaned_data.get('security_code')
        amount = self.cleaned_data.get('amount')
        expiration_date = self.cleaned_data.get('expiration_date')

        if not creditcard_number or len(creditcard_number) < 16:
            self._errors['creditcard_number'] = self.error_class([
                'We need 16 characters'])

        if not card_holder or len(card_holder) < 3:
            self._errors['card_holder'] = self.error_class([
                'We need more characters at name field'])

        if not security_code or len(security_code) < 3:
            self._errors['security_code'] = self.error_class([
                'We need 3 numbers'])


        if not amount or amount < 1:
            self._errors['amount'] = self.error_class([
                'We need an amount bigger than 1$ to be transfered'])

        if not expiration_date or expiration_date.date() < date.today():
            self._errors['expiration_date'] = self.error_class([
                'Date cannot be in the past'])  #pylint:disable=trailing-whitespace      
        # return any errors if found
        return self.cleaned_data
