from rest_framework import viewsets
from .serializers import CeosSerializer
from .models import Ceos


# Create your views here.

class CeosViewSet(viewsets.ModelViewSet):
    queryset = Ceos.objects.all().order_by('year_started')
    serializer_class = CeosSerializer
