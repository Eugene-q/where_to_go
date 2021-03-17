from django.contrib import admin
from .models import Location, Image
from django.utils.html import format_html
import traceback
from adminsortable2.admin import SortableInlineAdminMixin

class ImageInline(SortableInlineAdminMixin, admin.TabularInline):
    fields = ('title', 'image', 'get_preview', 'position')
    model = Image
    extra = 1
    readonly_fields = ['get_preview',]
    
    def get_preview(self, image):
        raito = image.image.width / image.image.height
        return format_html('<img src={url} width={width} height={height} />'.format(
            url=image.image.url,
            width=200 * raito,
            height=200
        ))
    
    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title',]
    
admin.site.register(Image)
