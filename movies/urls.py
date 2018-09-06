from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^movies', views.get, name='get'),
]