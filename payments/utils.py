import requests
import json
from requests.auth import HTTPBasicAuth
from datetime import datetime
import base64


class Credentials:
    consumer_key = 'WYkwf2eKIqWcw08HyTkukS6xErV4HEUW'
    consumer_secret = 'nsA7Q2L77TvyrHjl'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'


class Mpesa_Access_Token:
    response = requests.get(Credentials.api_URL, auth=HTTPBasicAuth(Credentials.consumer_key, Credentials.consumer_secret))
    mpesa_access_token = json.loads(response.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']


class Transaction_Request_Details:
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    OffSetValue = '0'
    passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'

    data_to_encode = Business_short_code + passkey + timestamp

    password = base64.b64encode(data_to_encode.encode())
    decoded_password = password.decode('utf-8')
