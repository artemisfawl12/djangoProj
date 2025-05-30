from django.urls import path, include
from . import views
from .views import stock_ticker_data, coin_ticker_data, multi_chart, multi_chart_coin, process, author_count, drf_upload_view, mentos_render,mentos_blog_render
from django.conf import settings
from django.conf.urls.static import static
import os

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
    path('mentos/',mentos_render,name="mentos mentors"),
    path('mentos/blog',mentos_blog_render,name="blog_list"),
    path('mentos/blog_form/', views.create_blog_post, name='create_blog_post'),
    path('about/', views.about_render, name='about_page'),

    path('check-password/', views.check_password, name='password_check'),

    path('mentos/categorzied/', views.mentos_categorized, name='categorizes'),
    path('ckeditor/', include('ckeditor_uploader.urls')),

    path('mentos/<slug:slug>/', views.blog_detail, name='blog_detail'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

