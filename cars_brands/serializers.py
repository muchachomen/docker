from rest_framework import serializers
from .models import CarBrand
from .models import Profile
from django.contrib.auth.models import User
class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = '__all__'

    def validate_country(self, value):
        valid_countries = ["Korea", "Germany", "Japan"]
        if value not in valid_countries:
            raise serializers.ValidationError("Valid country")
        return value


class ProfileSerializer(serializers.ModelSerializer):
        class Meta:
            model = Profile
            fields = ['bio', 'avatar']


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = User
        fields = ['username', 'email', 'profile', 'password']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create(**validated_data)
        Profile.objects.create(user=user, **profile_data)
        return user
