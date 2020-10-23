from django.urls import path
from . import views

urlpatterns = [
    # 어떤 앱의 views인지 명시하는 부분 빠짐
    path('', views.index, name='index'),
    path('sorry', views.sorry, name='sorry'),
]