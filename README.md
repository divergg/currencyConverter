# currencyConverter
Project implements API service for getting an actual currency rate.

# Project structure
Project consists of a API service (Django-Rest Framework) and a database (PostgreSQL), where data
on every request is recorded. Logging is enabled (in file general.log)
A side API is used to get currency rate. Default API is http://api.exchangeratesapi.io/v1/latest

# Database structure
Requests are recorded to a database with the following info:
datetime of request
currencies to compare
ammount
error message from side API (if any)


# Project endpoints:
http://django:8000/rate - check currency rate. 
Parameters - {'symbol_from': str, 'symbol_to': str, 'amount_from': decimal}

http://django:8000/statistics - recieve statistics on requests
http://django:8000/docs/ - documentation (SWAGGER)

# Screenshot from SWAGGER
![image](https://github.com/divergg/currencyConverter/tree/master/images/1.png)


# Launch procedure
1) Set up environment parameters:
   API_TOKEN - token from side API
   API_URL - url to side API
   DJANGO_KEY - django secret key
   SYMBOL_FROM = 'from' (parameter to be passed to API)
   SYMBOL_TO='to' (parameter to be passed to API)
   POSTHGRES_HOST, POSTGRES_PORT, POSTGRES_USERNAME, POSTGRES_PASSWORD
2) Initialize docker compose file
3) vualá

# Running tests
python manage.py tests


   






