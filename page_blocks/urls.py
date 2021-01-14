from django.conf.urls import url
from django.urls import include, path

from . import views


auth_urls = [
    url(r'^login$', views.authentication, name='authentication'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^registration$', views.registration, name='registration'),
]

app_name = 'page_blocks'
urlpatterns = [
    path('auth/', include(auth_urls)),
    path('', views.index, name='index'),
]
