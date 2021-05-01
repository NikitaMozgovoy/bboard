from .models import Bb, Rubric
from rest_framework import viewsets, permissions
from .serializers import BbSerializer, RubricSerializer, BbListRetrieveSerializer

class BbViewSet(viewsets.ModelViewSet):
    queryset = Bb.objects.all()
    permission_classes=[IsAuthenticated & IsAdminUser]
    serializer_class=BbSerializer

    action_to_serializer = {
        "list":BbListRetrieveSerializer,
        "retrieve":BbListRetrieveSerializer
    }
    def get_serializer_class(self):
        return self.action_to_serializer.get(
            self.action, self.serializer_class
        )

class RubricViewSet(viewsets.ModelViewSet):
    queryset = Rubric.objects.all()
    permission_classes=[IsAuthenticated & IsAdminUser]
    serializer_class=RubricSerializer

