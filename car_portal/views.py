from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializer import CarSerializer
from .models import Car


class CarListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, ]
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class CarDetailGenericView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    lookup_field = 'id'
