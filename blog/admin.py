from django.contrib import admin
from .models import Category, Post


class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')


class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    list_display = ('title', 'author', 'published', 'post_categories')
    ordering = ('author', 'published')
    search_fields = ('title', 'author__username')
    date_hierarchy = 'published'
    list_filter = ('author__username', 'categories__name')

    def post_categories(self, obj):
        return ", ".join([c.name for c in obj.categories.all().order_by("name")])
    post_categories.short_description = "Categorías"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
