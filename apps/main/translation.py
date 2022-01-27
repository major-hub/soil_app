from modeltranslation.decorators import register
from modeltranslation.translator import TranslationOptions

from main.models import Service, News, File, Laboratory, GalleryType, Employee, Document, History, Function


@register(Service)
class ServiceTranslation(TranslationOptions):
    fields = ('name', 'about')


@register(News)
class NewsTranslation(TranslationOptions):
    fields = ('title', 'short_description', 'body')


@register(File)
class FileTranslation(TranslationOptions):
    fields = ('name', )


@register(Laboratory)
class LaboratoryTranslation(TranslationOptions):
    fields = ('name', 'body')


@register(GalleryType)
class GalleryTranslation(TranslationOptions):
    fields = ('title', )


@register(Employee)
class EmployeeTranslation(TranslationOptions):
    fields = ('full_name', 'about')


@register(Document)
class DocumentTranslation(TranslationOptions):
    fields = ('name', )


@register(History)
class HistoryTranslation(TranslationOptions):
    fields = ('text', )


@register(Function)
class FunctionTranslation(TranslationOptions):
    fields = ('title', 'text')
