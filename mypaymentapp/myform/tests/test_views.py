""" This is the test file for the views """
from http import HTTPStatus
from django.test import TestCase
# from myform.views import CardFormNew


class ProcessPaymentTests(TestCase):
    """ This is the test class for the payment method """
    def test_process_payment(self):
        """ This is the test for the payment method"""
        response = self.client.get("")
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "", html=True)

    def test_process_creditcard_number(self):
        """ This is the test class for the creditcard_number field"""
        response = self.client.post("", data={"creditcard_number": "1234567890123445"})
        self.assertEqual(response.status_code, HTTPStatus.OK)


    def test_process_card_holder(self):
        """ This is the test class for the card_holder field"""
        response = self.client.post("", data={"card_holder":"yoshi"})
        self.assertEqual(response.status_code, HTTPStatus.OK)


    def test_process_security_code(self):
        """ This is the test class for the security_code field"""
        response = self.client.post("", data={"security_code":"123"})
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_process_amount(self):
        """ This is the test class for the amount field"""
        response = self.client.post("", data={"amount":"123"})
        self.assertEqual(response.status_code, HTTPStatus.OK)


    def test_process_expiration_date(self):
        """ This is the test class for the expiration_date field """
        response = self.client.post("", data={"expiration_date":"2020-10-10"})
        self.assertEqual(response.status_code, HTTPStatus.OK)
