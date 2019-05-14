from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'dashboard.html', views.home),
    url(r'user.html', views.user),
]
