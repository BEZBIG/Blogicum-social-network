from django.contrib import admin
from .models import Category, Location, Post


admin.site.empty_value_display = 'Не задано'

class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'category',
        'location',
        'is_published',
        'pub_date',
    )
    list_editable = (
        'category',
        'location',
        'is_published',
    )
    search_fields = ('title', 'text', 'author__username')
    list_filter = ('is_published', 'category', 'location', 'author')
    list_display_links = ('title',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title', 'slug')
    list_filter = ('is_published',)
    list_display_links = ('title',)

class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('name',)
    list_filter = ('is_published',)
    list_display_links = ('name',)

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)