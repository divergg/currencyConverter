import requests
import logging
from typing import Union
from rest_framework import status
from rest_framework.response import Response

from .config import (api_url, api_token, symbol_from_parameter,
                     symbol_to_parameter)

logger = logging.getLogger(__name__)

def handle_errors(data: list, allowed_fields: list):
    # Check that all fields are in request
    for field in allowed_fields:
        if field not in data:
            error_message = f'Missing {field} field'
            logger.error(error_message)
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

    # Look for unexpected fields
    unexpected_fields = [field for field in data if field not in allowed_fields]
    if unexpected_fields:
        error_message = f'Unexpected fields: {unexpected_fields}'
        logger.error(error_message)
        return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)


def send_rate_request(data: dict) -> Union[float, str]:

    symbol_from = data['symbol_from']
    symbol_to = data['symbol_to']
    amount_from = data['amount_from']

    payload = {
        f'{symbol_from_parameter}': symbol_from,
        f'{symbol_to_parameter}': symbol_to,
        'access_key': api_token,
    }
    result = requests.get(url=api_url, params=payload).json()
    if 'error' in result:
        return result['error']['code']
    rate = result['rates'][symbol_to] * amount_from
    return rate


