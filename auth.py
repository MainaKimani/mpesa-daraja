import requests
import json
import base64
from requests.auth import HTTPBasicAuth
from datetime import datetime

#timestamp
dateTime = datetime.now()
timestamp = dateTime.strftime('%Y%m%d%H%M%S')

#Till no. info
shortCode = '174379'
passKey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
password = shortCode + passKey + timestamp
encodedPassword = base64.b64encode(password.encode())
transactionType = 'CustomerPayBillOnline'

print (encodedPassword.decode("utf-8"))

#from the test app
key = 'lJHgZfP7Gt7dyRfyfasPISGXAF1iG2C4'
secret = 'IgJdZobwRL9Wm3Sk'
mpesa_sandbox ='https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

#send auth data to MPESA's endpoint
def authenticate():
    #get request
    response = requests.get(mpesa_sandbox, auth=HTTPBasicAuth(key, secret))
    
    #retrieve message
    obj_response = json.loads(response.text)
    print('Auth', obj_response)


def stk_push():
    payload = {
        "BusinessShortCode": shortCode,
        "Password": encodedPassword.decode("utf-8"),
        "Timestamp": timestamp,
        "TransactionType": transactionType,
        "Amount": 1,
        "PartyA": 254708374149,
        "PartyB": 174379,
        "PhoneNumber": 254707705021,
        "CallBackURL": "https://mydomain.com/path",
        "AccountReference": "CompanyXLTD",
        "TransactionDesc": "Payment of X" 
      }
    
    #get request
    response = requests.get(mpesa_sandbox, data = payload, auth=HTTPBasicAuth(key, secret))
    
    #retrieve message
    obj_response = json.loads(response.text)
    print('Message', obj_response)
    print('payload', payload)

stk_push()
input("Exit: ")