from django.contrib.auth.models import AbstractUser
# from django.db import models
# from phonenumber_field.modelfields import PhoneNumberField
# from .managers import UserManager


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

    def __str__(self) -> str:
        return self.username


# class CustomUser(AbstractUser):
#     # username = None
#     email = models.EmailField("Email Address", unique=True)
#     phone_number = PhoneNumberField(blank=True)

#     # USERNAME_FIELD = "email"
#     REQUIRE_FIELDS = []

#     objects = UserManager()

#     def __str__(self) -> str:
#         return self.username
