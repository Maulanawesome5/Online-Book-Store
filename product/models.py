from django.db import models
from django.utils.text import slugify


# Create your models here.
class AbstractProductModel(models.Model):
    """Class abstrak yang menampung beberapa properti data yang sama dan diwarisi oleh class lainnya."""
    __CATEGORY_DATA = (("writer", "Book Writer"),
                       ("publisher", "Book Publisher"),
                       ("book", "Book"),
                       )

    def get_category_data(self):
        """Method getter untuk mengakses variabel `__CATEGORY_DATA`"""
        return self.__CATEGORY_DATA

    def set_category_data(self, w=False, p=False, b=False):
        """
        Method setter untuk mengubah nilai atribut atau kolom `category_data`.
        Function ini berguna untuk query filter data.
        Parameter `w` artinya writer atau penulis buku.
        Parameter `p` artinya publisher atau penerbit buku.
        Parameter `b` artinya book atau produk buku.
        """
        try:
            if w == True:
                self.category_data = self.get_category_data()[0][0]
                self.save(force_insert=True, force_update=True)

            if p == True:
                self.category_data = self.get_category_data()[1][0]
                self.save(force_insert=True, force_update=True)

            if b == True:
                self.category_data = self.get_category_data()[2][0]
                self.save(force_insert=True, force_update=True)

        except:
            return False

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=255, editable=False)
    category_data = models.CharField(max_length=50, blank=True, editable=False)

    class Meta:
        abstract = True


class Writer(AbstractProductModel):
    """Class ini merupakan data model tentang seorang `penulis buku`."""
    name = models.CharField(max_length=100, unique=True)
    full_name = models.CharField(max_length=100, unique=True)
    about = models.TextField(blank=True, null=True)
    images = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.full_name)
        self.set_category_data(w=True)

        super(Writer, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Publisher(AbstractProductModel):
    """Class ini merupakan data model perusahaan `penerbit buku`."""
    name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    images = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.company_name)
        self.set_category_data(p=True)

        super(Publisher, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ["name"]


class Book(AbstractProductModel):
    """Class ini merupakan model untuk data `produk buku`"""
    title = models.CharField(max_length=255)
    writer = models.ForeignKey(Writer, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    years = models.IntegerField()
    description = models.TextField()
    cover_book = models.CharField(max_length=255, blank=True)
    price = models.IntegerField(default=0)
    avail_stock = models.IntegerField(default=0)
    isbn = models.CharField(max_length=255, blank=True)
    weight = models.FloatField(default=0.0)
    width = models.FloatField(default=0.0)
    length = models.FloatField(default=0.0)
    pages_count = models.IntegerField(default=0)
    is_discount = models.BooleanField(default=False)
    discount = models.IntegerField(default=0)
    price_discount = models.IntegerField(default=0)

    def is_discounted(self):
        """
        Function setter untuk memeriksa kondisi kolom field `is_discount`. Jika field
        tersebut bernilai True, maka akan mengeksekusi function `price_after_discount`.
        Jika `is_discount` bernilai False, maka fields `discount` dan `price_discount`
        akan di setting kembali menjadi nilai defaultnya.
        """
        if self.is_discount == True:
            self.price_after_discount()

        else:
            self.discount = 0
            self.price_discount = 0

    def price_after_discount(self):
        """
        Jika terdapat diskon, maka harga final produk adalah setelah dikurangi diskon.
        """
        self.price_discount = self.price - (self.price * self.discount / 100)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.set_category_data(b=True)
        self.is_discounted()

        super(Book, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
        # pass
