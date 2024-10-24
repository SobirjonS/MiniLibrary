from modeltranslation.translator import register, TranslationOptions
from . import models


@register(models.Banner)
class BannerTranslationOptions(TranslationOptions):
    fields = ('title',)


@register(models.AboutUs)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('description',)
    
    
@register(models.News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)
    