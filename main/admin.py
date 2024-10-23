from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models


@admin.register(models.AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    fieldsets = (
        (_('Uzbek'), {'fields': ('description_uz',)}),
        (_('Russian'), {'fields': ('description_ru',)}),
        (_('English'), {'fields': ('description_en',)}),
        (_('Image'), {'fields': ('image',)}),
    )
    

@admin.register(models.News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'title_ru', 'title_en')
    fieldsets = (
        (_('Uzbek'), {'fields': ('title_uz', 'description_uz')}),
        (_('Russian'), {'fields': ('title_ru', 'description_ru')}),
        (_('English'), {'fields': ('title_en', 'description_en')}),
        (_('Image'), {'fields': ('image',)}),
    )


admin.site.register(models.Library)
admin.site.register(models.Book)
admin.site.register(models.SocialMedia)