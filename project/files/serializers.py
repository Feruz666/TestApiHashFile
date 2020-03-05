from rest_framework import serializers
from rest_framework import exceptions
from .models import Files

class FileSerializer(serializers.Serializer):
    class Meta:
        model = Files
        fields = ['name', 'docfile', 'code_md5', 'code_sha256']