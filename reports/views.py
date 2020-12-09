from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet

from .models import Report
from .serializers import ReportSerializer


class ReportViewSet(ModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    http_method_names = [
        "get",
    ]
