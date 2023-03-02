import datetime
import random
import re

import requests
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken

from .models import MyUser


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


def generateOTP():
    return 666666
    # return random.randint(111111, 999999)


def isValid(s):
    Pattern = re.compile("(0|91)?[7-9][0-9]{9}")
    return Pattern.match(s)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['id', 'first_name', 'phone', 'image']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['first_name', 'phone']

    def validate(self, attrs):
        number = attrs['phone']
        data = MyUser.objects.filter(phone=attrs['phone']).first()

        if not isValid(number):
            raise serializers.ValidationError({"phone": "Phone number isn't valid"})
        elif data:
            raise serializers.ValidationError({'Error': 'User already registered'})
        return attrs

    def create(self, validated_data):

        user = MyUser.objects.create(
            first_name=validated_data['first_name'],
            phone=validated_data['phone'],
        )
        user.set_password(validated_data['phone'])
        user.save()

        return user


class GenerateOptSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=200)
    phone = serializers.CharField(max_length=15)

    def validate(self, attrs):
        number = attrs['phone']

        if not isValid(number):
            raise serializers.ValidationError({"phone": "Phone number isn't valid"})
        return attrs

    def create(self, validated_data):
        otp = generateOTP()
        now = datetime.datetime.now()
        date = now + datetime.timedelta(0, 180)
        user, created = MyUser.objects.get_or_create(phone=validated_data['phone'])
        user.otp = str(otp)
        user.first_name = validated_data['first_name']
        phone = validated_data['phone']
        user.otp_expire = date
        user.save()

        username = 'monandtex'
        password = 'a88^hSE^nM-9'
        sms_data = {
            "messages": [{"recipient": f"{phone}", "message-id": "abc000000003",
                          "sms": {"originator": "3700", "content": {"text": f"{otp}"}}}]}
        url = "http://91.204.239.44/broker-api/send"
        res = requests.post(url=url, headers={}, auth=(username, password), json=sms_data)
        return user


class LoginSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=15)

    class Meta:
        model = MyUser
        fields = ['phone']

    def validate(self, attrs):
        data = MyUser.objects.filter(phone=attrs['phone']).first()
        if not data:
            raise serializers.ValidationError({'Error': 'User not registered'})
        return attrs


class UpdatePhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    user_id = serializers.CharField(max_length=50)


class ConfirmUpdatePhoneSerializer(serializers.Serializer):
    phone = serializers.CharField(max_length=15)
    otp = serializers.CharField(max_length=50)

    # class Meta:
    #     model = MyUser
    #     fields = ['phone']

    # def validate(self, attrs):
    #     data = MyUser.objects.filter(phone=attrs['phone']).first()
    #     if not data:
    #                 raise serializers.ValidationError({'Error': 'User not registered'})
    #     return attrs
