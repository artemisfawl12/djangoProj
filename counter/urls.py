from django.urls import path
from . import views
from .views import stock_ticker_data

urlpatterns = [
    path('', views.count_characters, name='count_characters'),  # 기본 URL과 views.home 연결
    path('api/stocks/', stock_ticker_data, name='stock_ticker_data'),

]
