from rest_framework import serializers
from .models import *

class ReviewClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewClient
        fields = '__all__'


class ReviewFamousSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewFamous
        fields = '__all__'
        

class InfographicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infographic
        fields = '__all__'
        

class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = '__all__'
        

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
        

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        

class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'
        

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'
        
