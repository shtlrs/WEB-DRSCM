from rest_framework.serializers import ModelSerializer
from drscm.models import WorkSession


class WorkSessionSerializer(ModelSerializer):

    class Meta:
        model = WorkSession
        fields = ['id', 'start_timestamp', 'end_timestamp']