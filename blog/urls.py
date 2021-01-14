from django.urls import path
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:pk>', views.post_detail, name='post_detail'),
    path('write/', views.post_new, name='post_new'),
    path('edit/<int:pk>', views.post_edit, name='post_edit'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('delete/<int:pk>', views.post_del,name='post_del'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT})
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)