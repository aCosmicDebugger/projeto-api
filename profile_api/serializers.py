from rest_framework import serializers
from profile_api import models

class HelloSerializer(serializers.Serializer):
    """Serializa o campo nome para testar nossa APIView."""
    name = serializers.CharField(max_length=15)


class UserProfileSerializer(serializers.ModelSerializer):
    """ Serializa o profile do usuário """

    class Meta:
        model = models.UserProfile
        fields = ('id','email','name','password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style' :{'input_type':'password'}
            }
        }

    def create(self, validated_data):
        """ Cria e retorna um novo usuário """
        user = models.UserProfile.objects.create_user(
                email = validated_data['email'],
                name = validated_data['name'],
                password =validated_data['password']
        )

        return user

    def update(self, instance, validated_data):
        """ Lida com o update da conta """
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)
