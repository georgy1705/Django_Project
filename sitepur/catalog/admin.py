from django.contrib import admin
from .models import Articles, ArticlesImage, Gender, Subcategory, Brand


class ArticlesImageAdmin(admin.StackedInline):
    model = ArticlesImage


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    inlines = [ArticlesImageAdmin]
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Gender)
admin.site.register(Subcategory)
admin.site.register(Brand)






