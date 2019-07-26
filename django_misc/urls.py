from django.contrib import admin
from django.conf.urls import url, include


from app import views as app_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('app.app_urls')),
]
