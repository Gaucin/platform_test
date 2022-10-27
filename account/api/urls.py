from django.urls import path

from account.api.views import CustomerLoginView


urlpatterns = [
    path("login/", CustomerLoginView.as_view()),
]
