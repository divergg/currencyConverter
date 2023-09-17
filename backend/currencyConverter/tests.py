import json

from django.test import TestCase, Client
from rest_framework.test import APIRequestFactory
from rest_framework import status
from .models import CurrencyRateRequest
from .views import GetCurrencyRate, GetRequestsStat

class GetCurrencyRateTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = GetCurrencyRate.as_view()

    def test_get_currency_rate(self):
        data = {
            "symbol_from": "EUR",
            "amount_from": 100,
            "symbol_to": "USD",
        }

        data = json.dumps(data)

        # Send a POST request to the view
        request = self.factory.post('/rate', data, content_type='application/json')
        response = self.view(request)
        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check if the response contains the expected keys
        self.assertIn('rate', response.data)

        # Check if the request was saved in the database
        self.assertEqual(CurrencyRateRequest.objects.count(), 1)

    def test_invalid_currency_rate_request(self):
        # Define an invalid data payload for the POST request
        invalid_data = {
            "symbol_from": "EUR",
            "symbol_to": "USD",
        }

        invalid_data = json.dumps(invalid_data)
        request = self.factory.post('/rate', invalid_data, content_type='application/json')
        response = self.view(request)
        self.assertIn('error', response.data)

class GetRequestsStatTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = GetRequestsStat.as_view()

    def test_get_requests_stat(self):
        request = self.factory.get('/statistics')
        response = self.view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('requests', response.data)
