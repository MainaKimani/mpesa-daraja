
import requests

from .utils import Mpesa_Access_Token, Transaction_Request_Details


class STK_push:
    def initiate_STKpush(phone_number):
        access_token = Mpesa_Access_Token.validated_mpesa_access_token 
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": Transaction_Request_Details.Business_short_code,
            "Password": Transaction_Request_Details.decoded_password,
            "Timestamp": Transaction_Request_Details.timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": 1,
            "PartyA": phone_number,
            "PartyB": Transaction_Request_Details.Business_short_code,
            "PhoneNumber": phone_number,
            "CallBackURL": "https://callbackurl.free.beeceptor.com/",
            "AccountReference": "STK-TEST",
            "TransactionDesc": "Testing stk push"
        }
        res = requests.post(api_url, json=request, headers=headers)
        print (res.text)
        return res

    def stk_push_query():
        access_token = Mpesa_Access_Token.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
        headers = {"Authorization": "Bearer %s" % access_token}
        query_data = {
            "BusinessShortCode": Transaction_Request_Details.Business_short_code,
            "Password": Transaction_Request_Details.decoded_password,
            "Timestamp": Transaction_Request_Details.timestamp,
            "CheckoutRequestID": "ws_CO_22032023103134483707705021"
        }
        res = requests.post(api_url, json=query_data, headers=headers)
        response_data = res.json()
        print (response_data)
        return res