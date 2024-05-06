from django.contrib import admin
from .models import Writer, Publisher, Book


# Register your models here.
class ProductModelAdmin(admin.ModelAdmin):
    """Class untuk pengaturan data pada halaman admin"""
    readonly_fields = ["created", "updated", "slug", "category_data",]


admin.site.register(Writer, ProductModelAdmin)
admin.site.register(Publisher, ProductModelAdmin)
admin.site.register(Book, ProductModelAdmin)
