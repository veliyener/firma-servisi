from rest_framework import serializers
from .models import Company
from .messages import Messages


class CompanySerializer(serializers.ModelSerializer):
    tax_number = serializers.CharField(max_length=11, validators=[])

    class Meta:
        model = Company
        fields = ['id', 'title', 'tax_number', 'status', 'created_at', 'updated_at']
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']


class CompanyStatusUpdateSerializer(serializers.Serializer):
    status = serializers.CharField()

    def validate_status(self, value):
        if value not in ('active', 'passive'):
            raise serializers.ValidationError(Messages.INVALID_STATUS)
        return value