from django.urls import path

from events.api.views import EventView, PublicEventsView


urlpatterns = [
    path("", EventView.as_view()),
    path("public/", PublicEventsView.as_view()),
]
