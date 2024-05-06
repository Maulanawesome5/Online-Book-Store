from django.db import models


# Create your models here.
class Province(models.Model):
    province = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        return super(Province, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return "{}. {}".format(self.pk, self.province)


class City(models.Model):
    predicate_choices = (("Kabupaten", "Kabupaten"),
                         ("Kota", "Kota"))
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    predicate = models.CharField(max_length=25, choices=predicate_choices)
    city = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        return super(City, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return "{}.{}. {} {}".format(self.province.pk, self.pk, self.predicate, self.city)


class Subdistrict(models.Model):
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    predicate = models.CharField(max_length=50, default="Kecamatan")
    subdistrict = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        return super(Subdistrict, self).save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.province.pk}.{self.city.pk}.{self.pk} {self.predicate} {self.subdistrict}"
