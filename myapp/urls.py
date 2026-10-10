from django.urls import path
from .views import profile1, music

urlpatterns = [
    path("", profile1, name="profile1"),
    path("music", music, name="music")
]