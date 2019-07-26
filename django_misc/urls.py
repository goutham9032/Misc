from django.conf.urls import url
from django.contrib import admin

from app import views as app_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('app.app_urls')),
]
