from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import GenericViewSet

from .models import Data
from .serializers import DataSerializer


class DataViewSet(mixins.CreateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Data.objects.all()

        return Data.objects.filter(pk=pk)
