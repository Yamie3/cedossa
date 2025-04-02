from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Add this
from django.conf.urls.static import static  # Add this

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # All URLs delegated to main app
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)