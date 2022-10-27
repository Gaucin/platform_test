from django.urls import path

from rooms.api.views import RoomView


urlpatterns = [
    path("", RoomView.as_view()),
]
