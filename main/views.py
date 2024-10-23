from rest_framework.views import APIView
from rest_framework.response import Response

from . import serializers
from .import models


class MainAPIView(APIView):
    def get(self,request):
        data = {
            "about_us" : models.AboutUs.objects.all(), 
            "news" : models.News.objects.all(), 
            "library" : models.Library.objects.all(), 
            "book" : models.Book.objects.all(), 
            "socialmedia" : models.SocialMedia.objects.all(), 
        }

    
        serializer = serializers.MainSerializer(data, context={'request':request})
        return Response(serializer.data)
