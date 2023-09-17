import logging
from rest_framework import views
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema




from .utils import handle_errors, send_rate_request
from .models import CurrencyRateRequest

logger = logging.getLogger(__name__)


class GetCurrencyRate(views.APIView):

    ALLOWED_FIELDS = [
        'symbol_from',
        'amount_from',
        'symbol_to',
    ]

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'symbol_from': openapi.Schema(type=openapi.TYPE_STRING,
                                              description="Symbol of currency to convert from (i.e. EUR, etc.)"),
                'amount_from': openapi.Schema(type=openapi.TYPE_NUMBER, description="Amount to be converted"),
                'symbol_to': openapi.Schema(type=openapi.TYPE_STRING,
                                            description="Symbol of currency to convert to (i.e. USD, etc.)"),
            },
            required=['symbol_from', 'amount_from', 'symbol_to'],
        ),
        operation_description="Request to receive currency rate",
    )
    def post(self, request):

        data = request.data

        logger.info(f'Incoming request - {data}')

        # Handle possible errors
        errors = handle_errors(data, self.ALLOWED_FIELDS)
        if errors:
            return errors

        # Record request in DB
        request = CurrencyRateRequest.objects.create(**data)

        # Send request to an external server and get response
        response = send_rate_request(data=data)
        if type(response) is str:
            request.error_message = response
            key = 'error'
            logger.error(f'The external API returned an error - {response}')
        else:
            request.amount_to = response
            key = 'rate'
        request.save()
        return Response({key: response})


class GetRequestsStat(views.APIView):

    @swagger_auto_schema(operation_description='Get requests statistics')
    def get(self, request):
        stat = len(CurrencyRateRequest.objects.filter())
        logger.info(f'Requests for stats. Response - {stat}')
        return Response(
            {'requests': stat}
        )
















