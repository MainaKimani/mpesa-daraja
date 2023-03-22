from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.getAccessToken, name='access_token'),
    path('stk/', views.stk_push, name='stk_push'),
    path('stk/status', views.query_stk_status, name='stk_status'),
    path('callback/', views.STK_call_back_url.as_view(), name='stk-callback-url'),
    path('stk/call', views.callback_query, name='stk_callback'),
]
 