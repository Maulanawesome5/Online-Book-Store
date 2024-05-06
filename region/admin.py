from django.contrib import admin
from .models import Province, City, Subdistrict


# Register your models here.
class RegionAdminView(admin.ModelAdmin):
    """
    Model Admin class untuk mengatur tampilan halaman admin tabel `Region` (wilayah administrasi).
    """
    ordering = ["id",]


admin.site.register(Province, RegionAdminView)
admin.site.register(City, RegionAdminView)
admin.site.register(Subdistrict, RegionAdminView)
