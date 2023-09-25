from django.urls import path
from . import views

urlpatterns = [
    path('', views.qrng_page, name='qrng_page'),  # Handle the root URL ("/")
    # Other URL patterns for your app if needed
]

