from django.contrib import admin

# Register your models here.
from .models import Category, Product, Logo, MenuItem, SocialMediaLink, ProductComment, PagesTitle, BlogCategory, Blog
# Register your models here.

# admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'slug', 'is_active')  # Columns to display in the admin list
    list_filter = ('is_active',)  # Add a filter for the 'is_active' field
    search_fields = ('category_name', 'slug')  # Add a search box for 'name' and 'slug'
    prepopulated_fields = {'slug': ('category_name',)}  # Auto-fill slug field based on the name

admin.site.register(Product)
admin.site.register(ProductComment)

@admin.register(Logo)
class LogoAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'alt_text')

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent', 'position','order', 'is_active')
    list_filter = ('parent', 'position', 'is_active')
    ordering = ('order',)


@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display = ('platform', 'url', 'location', 'is_active')
    list_filter = ('location', 'is_active')
    search_fields = ('platform', 'url')


@admin.register(PagesTitle)
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'meta_title')


@admin.register(BlogCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date_posted', 'total_views')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('category', 'date_posted')