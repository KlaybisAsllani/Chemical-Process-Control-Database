from rest_framework import generics
from .models import Reactor
from .serializers import ReactorSerializer

class ReactorList(generics.ListAPIView):
    queryset = Reactor.objects.all()
    serializer_class = ReactorSerializer
