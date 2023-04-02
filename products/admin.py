from django.contrib import admin

from products.models import MainProduct, MainProduct2, Images, SubProduct


class SubProductImagesInline(admin.StackedInline):
    model = Images


class SubProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'main_product', 'create_at']
    readonly_fields = ['view_count']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [SubProductImagesInline]


class MainProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'create_at')
    readonly_fields = ['view_count']
    prepopulated_fields = {'slug': ('title',)}


class MainProduct2Admin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'create_at')
    readonly_fields = ['view_count']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(MainProduct, MainProductAdmin)
admin.site.register(MainProduct2, MainProduct2Admin)
admin.site.register(SubProduct, SubProductAdmin)
