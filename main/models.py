from django.db import models

class AboutUs(models.Model):
    image = models.ImageField(upload_to='AboutUs/')
    description = models.TextField()
    
    
    class Meta:
        verbose_name = "Biz haqimizda"
        verbose_name_plural = "Biz haqimizda" 
        

class Library(models.Model):
    image = models.ImageField(upload_to='Library/')
    
    
    class Meta:
        verbose_name = "Bizning kutubxona"
        verbose_name_plural = "Bizning kutubxona" 
        

class Book(models.Model):
    image = models.ImageField(upload_to='Books/')
    
    
    class Meta:
        verbose_name = "Kitob"
        verbose_name_plural = "Kitoblar" 
        
        
class News(models.Model):
    image = models.ImageField(upload_to='News/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    
    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar" 
        
        
class SocialMedia(models.Model):
    icon = models.ImageField(upload_to='SocialMedia/')
    link = models.TextField()
    
    
    class Meta:
        verbose_name = "Ijtimoiy tarmoq"
        verbose_name_plural = "Ijtimoiy tarmoqlar" 
        