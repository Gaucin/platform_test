from django.urls import path

from account.api.views import CustomerLoginView


urlpatterns = [
    path("", CustomerLoginView.as_view()),
]
