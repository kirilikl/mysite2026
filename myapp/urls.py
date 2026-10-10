from django.urls import path
from .views import profile1

urlpatterns = [
    path("", profile1, name="profile1")
]