from django.contrib import admin
from .models import Articles, ArticlesImage


class ArticlesImageAdmin(admin.StackedInline):
    model = ArticlesImage


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    inlines = [ArticlesImageAdmin]
    prepopulated_fields = {"slug": ("title",)}







