
from django.urls import path
from .views import home, webHook
urlpatterns = [
    path('', home),
    path('webhook/',webHook)
]