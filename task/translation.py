from modeltranslation.translator import TranslationOptions, register
from task import models


@register(models.Dish)
class ProductTranslation(TranslationOptions):
    fields = ('name', 'description')



