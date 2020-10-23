from django.contrib import admin
from django.urls import path, include 
# urls 분리에 사용되는 include 추가 import
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('myblog.urls')),
    path('accounts/', include('allauth.urls')),  # 추가
]