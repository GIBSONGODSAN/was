from rest_framework import serializers
from .models import Records

class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Records
        fields = ['value1', 'value3']