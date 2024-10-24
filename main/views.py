from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from .import models


class MainAPIView(APIView):
    def get(self,request):
        data = {
            "banner" : models.Banner.objects.all(), 
            "aboutus" : models.AboutUs.objects.all(), 
            "library" : models.Library.objects.all(), 
            "book" : models.Book.objects.all(), 
            "news" : models.News.objects.all(), 
            "socialmedia" : models.SocialMedia.objects.all(), 
        }

    
        serializer = serializers.MainSerializer(data, context={'request':request})
        return Response(serializer.data)
