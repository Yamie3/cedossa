from django.urls import path
from . import views
from django.conf.urls import handler404
handler404 = 'main.views.page_not_found'
from django.conf import settings  # Add this
from django.conf.urls.static import static  # Add this


app_name = 'main'  # Namespace for URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),  # Must match view name
    path('donate/', views.donate, name='donate'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)