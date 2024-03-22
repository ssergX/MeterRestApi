from rest_framework import generics
from .models import Data
from .serializers import DataSerializer


class DataViewSet(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class DataDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    lookup_field = 'id'
