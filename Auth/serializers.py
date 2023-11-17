from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import MyCustomUser


# User Seralizer, sérialise les données pour la BDD
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyCustomUser
        fields = ['id', 'first_name', 'username','last_name', 'email', 'password', 'team']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)

        instance.save()
        return instance