from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Log, CycleHours
from .serializers import LogSerializer, CycleHoursSerializer

class LogViewSet(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer

    @action(detail=True, methods=['get'])
    def get_by_id(self, request, pk=None):
        try:
            log = Log.objects.get(pk=pk)
            serializer = LogSerializer(log)
            return Response(serializer.data)
        except Log.DoesNotExist:
            return Response({"error": "Log not found"}, status=404)

class CycleHoursViewSet(viewsets.ModelViewSet):
    queryset = CycleHours.objects.all()
    serializer_class = CycleHoursSerializer
