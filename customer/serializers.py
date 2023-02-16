from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
import re


def isValid(s):
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(s)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        return token



class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=False,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )

    password = serializers.CharField(write_only=False, required=True, validators=[validate_password])
    # picture = serializers.ImageField(
    #         required=False
    # )
    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        extra_kwargs = {
            'first_name': {'required': False}
        }

    def validate(self, attrs):
        number = attrs['username']
        if not isValid(number):
            raise serializers.ValidationError({"phone": "Phone number isn't valid"})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
#            email=validated_data['email'],
#            first_name=validated_data['first_name']
        )


        user.set_password(validated_data['password'])
        user.save()
        # info = UserInfo.objects.create(
        #     user=user,
        # )
        # info.save()

        return user


class CheckSerializer(serializers.ModelSerializer):
    class Meta:
        model = CheckAccaunt
        fields = ['phone']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'picture', 'address')


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInfo
        fields = '__all__'

