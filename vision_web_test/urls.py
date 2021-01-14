from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)


tokens_url = [
    path('', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('verify/', TokenVerifyView.as_view()),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', include(tokens_url)),
    path('main_page/', include('page_blocks.urls')),
    path('', RedirectView.as_view(url='/main_page', permanent=True)),
]
