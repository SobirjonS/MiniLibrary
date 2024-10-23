from rest_framework import serializers
from . import models


class AboutUsSerializer(serializers.ModelSerializer):
    description = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = models.AboutUs
        fields = ['id', 'description', 'image_url']
        
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_description(self, obj):
        return {
            'uz': obj.description_uz,
            'ru': obj.description_ru,
            'en': obj.description_en
        }
        
        
class NewsSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    description = serializers.SerializerMethodField()
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = models.News
        fields = ['id', 'title', 'description', 'image_url']
        
    def get_title(self, obj):
        return {
            'uz': obj.title_uz,
            'ru': obj.title_ru,
            'en': obj.title_en
        }
        
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None

    def get_description(self, obj):
        return {
            'uz': obj.description_uz,
            'ru': obj.description_ru,
            'en': obj.description_en
        }
        
        
class LibrarySerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = models.Library
        fields = ['id', 'image_url']
        
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    
    
class BookSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
        
    class Meta:
        model = models.Book
        fields = ['id', 'image_url']
        
    def get_image_url(self,obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
    
    
class SocialMediaSerializer(serializers.ModelSerializer):
    icon_url = serializers.SerializerMethodField()
        
    class Meta:
        model = models.SocialMedia
        fields = ['id', 'icon_url', 'link']
        
    def get_icon_url(self,obj):
        request = self.context.get('request')
        if obj.icon:
            return request.build_absolute_uri(obj.icon.url)
        return None
    
    
class MainSerializer(serializers.ModelSerializer):
    aboutus = AboutUsSerializer(many=True, read_only=True)
    news = NewsSerializer(many=True, read_only=True)
    library = LibrarySerializer(many=True, read_only=True)
    book = BookSerializer(many=True, read_only=True)
    socialmedia = SocialMediaSerializer(many=True, read_only=True)
        
    class Meta:
        model = models.News
        fields = ['aboutus', 'news', 'library', 'book', 'socialmedia']