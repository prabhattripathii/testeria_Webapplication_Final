# from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ('title', 'author', 'category__name')
    # prepopulated_fields = {'slug': ('title',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)
