from django.urls import path
from . import views

urlpatterns = [
    path('', views.count_characters, name='count_characters'),  # 기본 URL과 views.home 연결
]
