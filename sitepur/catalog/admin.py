from django.contrib import admin
from .models import Articles, ArticlesImage, Gender, Subcategory, Brand, Category, Size
from django.utils.safestring import mark_safe


class ArticlesImageAdmin(admin.StackedInline):
    model = ArticlesImage

class SizeAdmin(admin.StackedInline):
    model = Size

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}

@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    inlines = [ArticlesImageAdmin, SizeAdmin]
    list_display = ('title', 'slug', 'price', 'image_show', 'available')
    list_filter = ('available',)
    list_editable = ('price', 'available')
    prepopulated_fields = {"slug": ("title",)}

    def image_show(self, obj):
        if obj.img_thumbnail:
            return mark_safe("<img src='{}' width='60' />".format(obj.img_thumbnail.url))
        return "None"

    image_show.__name__ = "Картинка"


admin.site.register(Gender)
admin.site.register(Subcategory)
admin.site.register(Brand)








