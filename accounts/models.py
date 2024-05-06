from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class CustomUser(AbstractUser):
    """
    Class yang dikustom sendiri oleh developer untuk membuat tabel di database.
    Mewarisi dari class bawaan Django yaitu `AbstractUser`.
    Field yang tersedia didalamnya adalah:
        - username (wajib)
        - password (wajib)
        - first_name
        - last_name
        - email
        - is_staff
        - is_active
        - date_joined
    """
    pass

    def __str__(self) -> str:
        return self.username


# class AddressUser(models.Model):
#     """
#     Class ini akan menjadi tabel `alamat_rumah` user di database.
#     Dibuat terpisah karena tabel user bawaan dari Django tidak menyediakan kolom khusus
#     seperti nomor telpon, alamat rumah, upload foto, dsb.
#     """
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     address = models.CharField(max_length=255, blank=True, null=True)
