from django.contrib import admin

from .models import Post, Category, Location



class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'created_at',
        'is_published',
        'author',
        'location',
        'category'
    )
    list_editable = (
        'is_published',
        'category'
    )  


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'slug',
        'description'
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)