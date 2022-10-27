from django.urls import include, path


urlpatterns = [
    path("rooms/", include("rooms.api.urls")),
    path("events/", include("events.api.urls")),
    path("booking/", include("booking.api.urls")),
    path("account/", include("account.api.urls")),
]
