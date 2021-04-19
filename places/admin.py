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
        return format_html('<img src={url} height={max_height} />',
            url=image.image.url,
            max_height=200 if image.image.height > 200 else image.image.height,
        )
    
    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    inlines = [
        ImageInline,
    ]
    search_fields = ['title',]
    
admin.site.register(Image)
