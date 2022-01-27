from django.contrib import admin
from django.utils.translation import gettext as _

from main.models import File, History, Employee, News, HistoryImages, NewsImage, Contact, Document, DocumentImages, \
    GalleryType, Gallery, Laboratory, LaboratoryImage, Partner, Service, ServiceImages, Function, Static


class HistoryImagesAdmin(admin.TabularInline):
    model = HistoryImages
    fk_name = 'history'
    autocomplete_fields = (_('image'), )


class HistoryAdmin(admin.ModelAdmin):
    inlines = [HistoryImagesAdmin, ]
    list_display = (_('text'), )
    search_fields = ('text', )


class NewsImageAdmin(admin.TabularInline):
    model = NewsImage
    fk_name = 'news'
    autocomplete_fields = ('image',)


class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImageAdmin, ]
    list_display = (_('title'), _('short_description'))
    readonly_fields = (_('view_count'), )
    search_fields = ('title', 'short_description')


class FileAdmin(admin.ModelAdmin):
    list_display = [_('name'), ]
    search_fields = ('name', 'id')


class EmployeeAdmin(admin.ModelAdmin):
    list_display = [_('full_name'), ]
    search_fields = ('full_name', )


class ContactAdmin(admin.ModelAdmin):
    list_display = [_('full_name'), _('email'), _('phone_number')]
    search_fields = ('full_name', 'email', 'phone_number')


class DocumentImageAdmin(admin.TabularInline):
    model = DocumentImages
    fk_name = 'document'
    autocomplete_fields = ('image',)


class DocumentAdmin(admin.ModelAdmin):
    inlines = [DocumentImageAdmin, ]
    list_display = [_('name'), 'link1', 'link2']
    search_fields = ('name', 'link1')


class GalleryTypeAdmin(admin.ModelAdmin):
    list_display = (_('title'), )


class GalleryAdmin(admin.ModelAdmin):
    list_display = (_('type'), )


class LaboratoryImageAdmin(admin.TabularInline):
    model = LaboratoryImage
    fk_name = 'laboratory'
    autocomplete_fields = ('image',)


class LaboratoryAdmin(admin.ModelAdmin):
    inlines = [LaboratoryImageAdmin, ]
    list_display = (_('name'), )
    search_fields = ('name', )


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('name', )
    search_fields = ('name', )


class ServiceImageAdmin(admin.TabularInline):
    model = ServiceImages
    fk_name = 'service'
    autocomplete_fields = ('image',)


class ServiceAdmin(admin.ModelAdmin):
    inlines = [ServiceImageAdmin, ]
    list_display = (_('name'), )
    search_fields = ('name', )


class FunctionAdmin(admin.ModelAdmin):
    list_display = (_('title'), )
    search_fields = ('title', )


class StaticAdmin(admin.ModelAdmin):
    list = ('key', 'value')


admin.site.register(File, FileAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Document, DocumentAdmin)
admin.site.register(GalleryType, GalleryTypeAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Laboratory, LaboratoryAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Function, FunctionAdmin)
admin.site.register(Static, StaticAdmin)
admin.site.site_header = _('Soil University Admin')
admin.site.site_title = _('Soil University')
admin.site.index_title = _('Welcome to Soil Research Portal')
