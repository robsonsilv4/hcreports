from rest_framework.serializers import ModelSerializer
from users.serializers import UserSerializer

from .models import Report, ReportResponse


class ReportResponseSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = ReportResponse
        fields = [
            "message",
            "author",
        ]


class ReportSerializer(ModelSerializer):
    author = UserSerializer(read_only=True)
    supervisors = UserSerializer(read_only=True, many=True)
    responses = ReportResponseSerializer(read_only=True, many=True)

    class Meta:
        model = Report
        fields = [
            "message",
            "author",
            "supervisors",
            "responses",
        ]
