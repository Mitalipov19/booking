from .models import *
from modeltranslation.translator import TranslationOptions,register


@register(Hotel)
class ProductTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'hotel_description', 'country', 'city', 'address')


@register(Room)
class ProductTranslationOptions(TranslationOptions):
    fields = ('room_description',)