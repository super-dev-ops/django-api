from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('postinfo/<int:pk>', views.post_detail),
    path('postinfo/<int:pk>/pretty', views.post_detail_pretty),
    path('posts/pretty', views.list_posts_pretty),
    path('posts/', views.list_posts),
    path('summernote/', include('django_summernote.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)