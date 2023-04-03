from django.contrib import admin

from products.models import MainProduct, MainProduct2, SubProductGallery, SubProduct, MainProductGallery


class SubProductImagesInline(admin.StackedInline):
    model = SubProductGallery


class MainProductImagesInline(admin.StackedInline):
    model = MainProductGallery


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
    inlines = [MainProductImagesInline]


admin.site.register(MainProduct, MainProductAdmin)
admin.site.register(MainProduct2, MainProduct2Admin)
admin.site.register(SubProduct, SubProductAdmin)
