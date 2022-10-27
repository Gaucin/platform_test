from rest_framework.generics import CreateAPIView, ListCreateAPIView

from rooms.models import Room
from rooms.api.serializers import RoomSerializer


class RoomView(ListCreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
