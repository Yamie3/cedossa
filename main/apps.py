from django.apps import AppConfig
from django.urls import path, include


#router = DefaultRouter()
#router.register(r'contact-messages', ContactMessageViewSet)

#urlpatterns = [
    #path('api/', include(router.urls)),

class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = 'Main Application'

class YourAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'

    #def ready(self):
        #import your_app.signals  # noqa