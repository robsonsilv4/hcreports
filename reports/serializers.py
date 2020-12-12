from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from .models import Report, ReportResponse


class UserReportSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = [
            "first_name",
            "last_name",
            "email",
        ]


class ReportResponseSerializer(ModelSerializer):
    author = UserReportSerializer(read_only=True)

    class Meta:
        model = ReportResponse
        fields = [
            "message",
            "author",
        ]


class ReportSerializer(ModelSerializer):
    author = UserReportSerializer(read_only=True)
    supervisors = UserReportSerializer(read_only=True, many=True)
    responses = ReportResponseSerializer(read_only=True, many=True)

    class Meta:
        model = Report
        fields = [
            "message",
            "author",
            "supervisors",
            "responses",
        ]
