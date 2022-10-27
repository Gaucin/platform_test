from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView

from events.models import Event
from events.api.serializers import EventSerializer


class EventView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class PublicEventsView(ListAPIView):
    queryset = Event.objects.filter(type=1)
    serializer_class = EventSerializer

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)
