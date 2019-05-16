from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'base.html', views.home),
    url(r'scans.html', views.scans),
]

#if settings.DEBUG:
   # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)