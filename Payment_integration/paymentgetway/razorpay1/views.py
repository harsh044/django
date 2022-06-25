from django.http.response import HttpResponse
from django.shortcuts import render
import razorpay

from paymentgetway.settings import RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY

# Create your views here.
client = razorpay.Client(auth=(RAZORPAY_API_KEY, RAZORPAY_API_SECRET_KEY))
def home(request):

    DATA = {
        "amount": 50000,
        "currency": "INR",
        "payment_capture":1,
        # "receipt": "receipt#1",
        # "notes": {
        #     "key1": "value3",
        #     "key2": "value2"
        # }
    }
    payment_order = client.order.create(data=DATA)
    payment_order_id = payment_order['id']
    context={
        'amount':500,
        'api_key':RAZORPAY_API_KEY,
        'order_id':payment_order_id
    }
    return render(request,"index.html",context)