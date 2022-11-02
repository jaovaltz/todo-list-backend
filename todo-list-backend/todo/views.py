from rest_framework import viewsets
from .models import ToDo
from .serializers import TodoSerializer

class TodoViewset(viewsets.ModelViewSet):
  queryset = ToDo.objects.all()
  serializer_class = TodoSerializer