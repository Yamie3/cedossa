from django.urls import path
from . import views
from django.conf.urls import handler404
handler404 = 'main.views.page_not_found'
from django.conf import settings  # Add this
from django.conf.urls.static import static  # Add this


app_name = 'main'  # Namespace for URLs

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('donate/', views.donate, name='donate'),
    path('autism_support/', views.autism_support, name='autism_support'),
    path('down_syndrome_support/', views.down_syndrome_support, name='down_syndrome_support'),
    path('our_programs/', views.programs, name='our_programs'),
    path('contact/', views.contact, name='contact'),
    path('contact-success/', views.contact_success, name='contact_success'),
    path('events/', views.events, name='events'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)