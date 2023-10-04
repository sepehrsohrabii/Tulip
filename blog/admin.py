from django.contrib import admin

from blog.models import Blog


# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "status", "create_at"]
    prepopulated_fields = {"slug": ("title", )}


admin.site.register(Blog, BlogAdmin)
