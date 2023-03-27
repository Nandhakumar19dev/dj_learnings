# from drf_explore.models import Project
from drf_explore.models import Project
from rest_framework import serializers

class ProjectSerializer(serializers.ModelSerializer):
    def to_internal_value(self, data, *args, **kwargs):

        return super().to_internal_value(data, *args, **kwargs)

    class Meta:
        model = Project
        fields = "__all__"
