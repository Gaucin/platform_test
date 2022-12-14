from rest_framework.serializers import ModelSerializer

from events.models import Event


class EventSerializer(ModelSerializer):
    class Meta:
        model = Event
        fields = (
            "id",
            "description",
            "type",
            "room",
        )
