from django.urls import path


urlpatterns = [
    path("", LoginGuestView.as_view()),
]
