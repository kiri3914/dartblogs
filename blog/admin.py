from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'author', 'created_at', 'photo', 'views', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('slug',)
    list_filter = ('title', 'created_at')
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'author', 'content', 'photo', 'views', 'category', 'tags')
    # readonly_fields = ('time_create', 'time_update', 'get_html_photo')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag)

admin.site.site_title = 'Админ-панель сайта о Аниме'
admin.site.site_header = 'Админ-панель сайта о Манге'
