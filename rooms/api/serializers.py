from rest_framework.serializers import ModelSerializer

from rooms.models import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "id",
            "name",
            "capacity",
        )
