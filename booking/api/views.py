from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView

from booking.models import Booking


class BookingView(CreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
