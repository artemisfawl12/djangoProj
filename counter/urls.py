from django.urls import path
from . import views
from .views import stock_ticker_data, coin_ticker_data, multi_chart, multi_chart_coin, process

urlpatterns = [
    path('', views.count_characters, name='count_characters'),  # 기본 URL과 views.home 연결
    path('api/stocks/', stock_ticker_data, name='stock_ticker_data'),
    path('api/coins/',coin_ticker_data, name="coin_ticker_data"),
    path('api/multichart/<str:ticker>/',multi_chart, name="multichart_stock"),
    path('api/multicoinchart/<str:ticker>/',multi_chart_coin, name="multichart_coin"),
    path('process/', process, name="author_revenue_calculate")

]
