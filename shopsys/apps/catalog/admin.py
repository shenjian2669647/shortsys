from django.contrib import admin
from shopsys.apps.catalog.models import Category, Product
from shopsys.apps.catalog.forms import ProductAdminForm


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm
    list_display = ("name", "price", "old_price", "created_at", "updated_at",)
    list_display_links = ("name",)
    list_per_page = 50
    ordering = ["-created_at"]
    search_fields = ["name", "description", "meta_keywords", "meta_description"]
    exclude = ("created_at", "updated_at",)
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at",)
    list_display_links = ("name",)
    list_per_page = 20
    ordering = ["name"]
    search_fields = ["name", "description", "meta_keywords", "meta_description"]
    exclude = ("created_at", "updated_at",)
    prepopulated_fields = {"slug": ("name",)}
