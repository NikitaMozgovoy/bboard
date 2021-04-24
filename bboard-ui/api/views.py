from rest_framework import viewsets
from django.shortcuts import render
from .serializers import BbSerializer, BbRubricSerializer, BbListRetrieveSerializer
from bboard.models import Bb, Rubric

class BbViewSet(viewsets.ModelViewSet):

    queryset = Bb.objects.all()
    serializer_class = BbListRetrieveSerializer

    
    # action_to_serializer = {
    #     "list": BbListRetrieveSerializer,
    #     "retrieve": BbListRetrieveSerializer
    # }

    # def get_serializer_class(self):
    #     return self.action_to_serializer.get(self.action, self.serializer_class)

class BbRubricViewSet(viewsets.ModelViewSet):
    querysett = Rubric.objects.all()
    serializer_class = BbRubricSerializer

        
def index(request):
    return render(request, 'index.html', {})