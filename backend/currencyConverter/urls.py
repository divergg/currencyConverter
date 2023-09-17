from django.urls import path

from . import views

urlpatterns = [
    path('rate', views.GetCurrencyRate.as_view(), name='rate'),
    path('statistics', views.GetRequestsStat.as_view(), name='statistics')
]