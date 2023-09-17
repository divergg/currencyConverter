import os
from dotenv import load_dotenv

load_dotenv()


api_token = os.getenv('API_TOKEN')
api_url = os.getenv('API_URL')
symbol_from_parameter = os.getenv('SYMBOL_FROM')
symbol_to_parameter = os.getenv('SYMBOL_TO')

