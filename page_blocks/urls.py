from django.urls import path

from . import views


app_name = 'page_blocks'
urlpatterns = [
    path('', views.index, name='index'),
]
