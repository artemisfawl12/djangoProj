from django.urls import path
from . import views
from .views import stock_ticker_data, coin_ticker_data, multi_chart, multi_chart_coin, process, author_count, drf_upload_view

urlpatterns = [
    path('', views.author_count, name='author_count'),  # 기본 URL과 views.home 연결
    path('api/stocks/', stock_ticker_data, name='stock_ticker_data'),
    path('api/coins/',coin_ticker_data, name="coin_ticker_data"),
    path('api/multichart/<str:ticker>/',multi_chart, name="multichart_stock"),
    path('api/multicoinchart/<str:ticker>/',multi_chart_coin, name="multichart_coin"),
    path('process/', process, name="author_revenue_calculate"),
    path('returnnum/', views.return_num , name="return number"),
    path('returnnum_bubang/', views.return_num_bubang , name="return number"),
    path('api/upload/', drf_upload_view),
    path('api/progress/', views.get_progress),
    path('api/result/', views.get_result),
    path('returnnum_chartscan/', views.return_num_chartscanner , name="return number for chartscanner"),
    path('index_prob/', views.index_prob , name="problem for hastag"),

]
