from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static


urlpatterns = [
    path('', include('qrng_app.urls')),  # Define root URL pattern
    path('admin/', admin.site.urls, name='admin'),
    path('qrng/', include('qrng_app.urls')),
]


