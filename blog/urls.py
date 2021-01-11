from django.urls import path
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:pk>/', views.post_detail, name='post_detail'),
    path('write/', views.post_new, name='post_new'),
    path('edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)