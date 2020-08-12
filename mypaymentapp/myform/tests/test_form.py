""" This is the test file for the form """
from http import HTTPStatus
from django.test import TestCase
from myform.forms import CardFormNew


class CardFormNewTestCase(TestCase):
    """ This is the test class for the form """
    #Credit card number TEST
    def test_clean_creditcard_number(self):
        """ This is the test for creditcard_number"""
        response = self.client.post("", data={"creditcard_number": "12345678901234"})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "We need 16 characters", html=True)

    def test_creditcard_number(self):
        """ This is the test for creditcard_number"""
        form = CardFormNew(data={"creditcard_number": "12345678901234"})
        self.assertEqual(form.errors["creditcard_number"], ["We need 16 characters"])
    #card_holder TEST
    def test_card_holder(self):
        """ This is the test for card_holder"""
        form = CardFormNew(data={"card_holder": "mi"})
        self.assertEqual(form.errors["card_holder"], ["We need more characters at name field"])

    def test_clean_card_holder(self):
        """ This is the test for card_holder"""
        response = self.client.post("", data={"card_holder": "mi"})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "We need more characters at name field", html=True) #pylint:disable=trailing-whitespace
    # security_code TEST
    def test_security_code(self):
        """ This is the test for security_code"""
        form = CardFormNew(data={"security_code": "12"})
        self.assertEqual(form.errors["security_code"], ["We need 3 numbers"])

    def test_clean_security_code(self):
        """ This is the test for security_code"""
        response = self.client.post("", data={"security_code": "12"})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "We need 3 numbers", html=True)
    #amount TEST
    def test_amount(self):
        """ This is the test for amount"""
        form = CardFormNew(data={"amount": "0.1"})
        self.assertEqual(form.errors["amount"], #pylint:disable=trailing-whitespace
                         ["We need an amount bigger than 1$ to be transfered"])

    def test_clean_amount(self):
        """ This is the test for amount"""
        response = self.client.post("", data={"amount": "0.1"})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, #pylint:disable=trailing-whitespace
                            "We need an amount bigger than 1$ to be transfered", html=True) #pylint:disable=trailing-whitespace  
    #expiration_date TEST
    def test_expiration_date(self):
        """ This is the test for expiration_date"""
        form = CardFormNew(data={"expiration_date": "2020-06-01"})
        self.assertEqual(form.errors["expiration_date"], ["Date cannot be in the past"])

    def test_clean_expiration_date(self):
        """ This is the test for expiration_date"""
        response = self.client.post("", data={"expiration_date": "2020-06-01"})
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Date cannot be in the past", html=True) #pylint:disable=trailing-whitespace
    