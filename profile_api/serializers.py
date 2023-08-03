from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializa o campo nome para testar nossa APIView."""
    name = serializers.CharField(max_length=15)
