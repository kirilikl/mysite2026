from django.urls import path
from .views import my_page, my_page2

urlpatterns = [
    path("", my_page, name="my_page"),
    path("user2", my_page2, name="mypage")
]