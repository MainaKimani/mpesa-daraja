from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

import requests

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from payments.api.serializers import TransactionSerializer
from payments.models import Transaction
from payments.stk import STK_push
from payments.utils import Mpesa_Access_Token


class STK_call_back_url(CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [AllowAny]

    def create(self, request):
         print(request.data)
         return HttpResponse("data sent")

         """
         {'Body': 
            {'stkCallback': 
                {'MerchantRequestID': '3792-1185393-1', 
                 'CheckoutRequestID': 'ws_CO_22032023114721322707705021', 
                 'ResultCode': 1032, 
                 'ResultDesc': 'Request cancelled by user'
                }
            }
         }
        """


def getAccessToken(request):
    access_token = Mpesa_Access_Token.validated_mpesa_access_token
    return HttpResponse(access_token)

def stk_push(request):
    """ Initiate STK Push request."""
    response = STK_push.initiate_STKpush(phone_number="254707705021")
    return HttpResponse("Request sent to customer: " + response.text)

def query_stk_status(checkout_request_id):
        """ query the status of the STK-push transaction."""
        response = STK_push.stk_push_query()
        return HttpResponse("Transaction status: " + response.text)

def callback_query(request):
        api_url = "https://a5c1-41-139-208-45.eu.ngrok.io/callback/"
        query_data = {
            'Body': 
            {'stkCallback': 
                {'MerchantRequestID': '3792-1185393-1', 
                 'CheckoutRequestID': 'ws_CO_22032023114721322707705021', 
                 'ResultCode': 1032, 
                 'ResultDesc': 'Request cancelled by user'
                }
            }
        }
        res = requests.post(api_url, json=query_data)
        
        return HttpResponse("Transaction status: ")
