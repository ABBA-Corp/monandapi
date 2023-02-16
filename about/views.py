from django.shortcuts import render
from .serializers import *
from rest_framework import viewsets

class InfographicView(viewsets.ModelViewSet):
    queryset = Infographic.objects.all()
    serializer_class = InfographicSerializer
    

class RewiewFamousView(viewsets.ModelViewSet):
    queryset = ReviewFamous.objects.all()
    serializer_class = ReviewFamousSerializer


class ReviewClientView(viewsets.ModelViewSet):
    queryset = ReviewClient.objects.all()
    serializer_class = ReviewClientSerializer


class SliderView(viewsets.ModelViewSet):
    queryset = Slider.objects.all()
    serializer_class = SliderSerializer


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class PartnerView(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer


class AboutView(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
