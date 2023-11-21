from django.contrib import admin  #imports the Django admin site that is included by default in Django projects.
from django.urls import path  , include # imports two functions from the django.urls module that are used to define URL patterns.
from django.conf.urls.static import static #imports the static() function that is used to serve media files during development.
from . import settings #imports the settings module from your project's root directory.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , include('store.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
