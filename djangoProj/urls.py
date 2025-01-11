"""
URL configuration for djangoProj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from counter.views import show_chart
from counter.views import show_tickersearch, delete_file, statistic_view, file_del_byip, coin_tickersearch, multi_result_coin, review_view, review_view_auth
from counter.views import multi_result
urlpatterns = [
    path('admin/', admin.site.urls),
    path('chart/',show_chart, name="show_chart" ),
    path('', include('counter.urls')),
    path('tickersearch/',show_tickersearch, name="show_tickersearch"),
    path('delete_file/',delete_file,name='delete_chart_file'),
    path('statistic/',statistic_view, name='statistics'),
    path('delete-html/', file_del_byip, name='delete_html'),
    path('multi/',multi_result, name="multi form"),
    path('cointickersearch/', coin_tickersearch, name="show_cointickersearch"),
    path('coinmulti/',multi_result_coin, name="multi_result_coin_form"),
    path('review/',review_view,name="review page"),
    path('reviewauth/',review_view_auth,name="review page for author")


]
