from django.contrib import admin
from django.urls import path, include
from subscriptions.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('subscriptions/', include('subscriptions.urls')),
]
