from django.urls import path

from booking.api.views import BookingView


urlpatterns = [
    path("", BookingView.as_view()),
]
