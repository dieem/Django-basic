#기본 path 함수를 사용하기 위해 똑같이 해당 기능을 import
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# 여기는 동일한 폴더에 있는 views이므로
# from .(현재폴더) import views 로 사용

urlpatterns = [
    path('', views.home, name='home'),
    path('create10/', views.create10, name='create10'),
    path('<int:post_id>/', views.detail, name="detail"),
    path('new/', views.new, name="new"),
    path('<int:post_id>/edit/', views.edit, name='edit'),
    path('<int:post_id>/delete/', views.delete, name="delete"),
    path('<int:post_id>/comments/create/', views.comments_create, name='comments_create'),
    path('<int:post_id>/comments/<int:comment_id>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:post_id>/comments/<int:comment_id>/update/', views.comments_update, name='comments_update'),
    path('<int:post_id>/like/', views.like, name='like'),  # 좋아요 기능
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)