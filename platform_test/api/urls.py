from django.urls import include, path


urlpatterns = [
    path("rooms/", include("cabs.api.urls")),
    path("events/", include("trips.api.urls")),
    path("booking/", include("trips.api.urls")),
    path("account/", include("account.api.urls")),
]
