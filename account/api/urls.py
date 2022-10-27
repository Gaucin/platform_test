from django.urls import path


urlpatterns = [
    path("customer/login/", LoginGuestView.as_view()),
]