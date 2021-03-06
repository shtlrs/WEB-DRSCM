from rest_framework import serializers
from drscm.models import WorkSession, Project


class WorkSessionSerializer(serializers.ModelSerializer):

    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all(), many=False)
    owner = serializers.ReadOnlyField(source="owner.email")

    class Meta:
        model = WorkSession
        fields = ["id", "start_timestamp", "end_timestamp", "owner", "project"]
