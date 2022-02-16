from rest_framework import generics 
from .models import Gift, Information 
from .serializers import GiftSerializer, InformationSerializer 
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly

class GiftList(generics.ListCreateAPIView):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class GiftDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Gift.objects.all()
    serializer_class = GiftSerializer
    permission_classes = [IsOwnerOrReadOnly]


class InformationList(generics.ListCreateAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class InformationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Information.objects.all()
    serializer_class = InformationSerializer
    permission_classes = [IsOwnerOrReadOnly]