"""streameventviewer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from stream_service.views import (get_favorite_streamer, get_stream, login,
                                  WebHookView, logout_view)

urlpatterns = [
    path(r'streamer/', get_favorite_streamer, name='favorite-streamer'),
    path(r'stream/', get_stream, name='stream'),
    path(r'', login, name='login'),
    path(r'logout/', logout_view, name='logout'),
    path(r'callback/', WebHookView.as_view(), name='callback'),
    path('admin/', admin.site.urls),
    path(r'', include('social_django.urls'), name='social'),
]
