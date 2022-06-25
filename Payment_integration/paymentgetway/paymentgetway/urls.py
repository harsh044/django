from django.contrib import admin
from django.urls import path,include
from razorpay1 import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('razorpay1.urls')),
]
# ID:pass::admin