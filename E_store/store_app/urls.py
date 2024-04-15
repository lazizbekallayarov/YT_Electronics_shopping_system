from django.urls import path
from store_app.views import Base

urlpatterns = [
    path('base/', Base, name='base'),
]