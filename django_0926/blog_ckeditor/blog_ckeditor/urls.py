from django.contrib import admin
from django.urls import path
import blogapp.views
from django.conf.urls import include # add
from django.conf import settings # add
from django.conf.urls.static import static # add

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.index, name='index'),
    path('blogMain/', blogapp.views.blogMain, name='blogMain'),
    path('blogMain/createBlog/', blogapp.views.createBlog, name='createBlog'),
    path('ckeditor/', include('ckeditor_uploader.urls')), # add
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # add
