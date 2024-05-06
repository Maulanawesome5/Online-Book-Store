from django.contrib.auth.decorators import login_required, permission_required
from django.db.models import Q
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, DetailView, RedirectView
from typing import Any
from .models import Book, Writer, Publisher


# Create your views here.
class IndexProductView(ListView):
    """
    Class View untuk menampilkan halaman Beranda produk.
    """
    template_name = "product/index.html"
    model = Book
    context_object_name = "Books"
    extra_context = {"page_title": "Produk", "website": "Toko Buku"}

    def get_queryset(self):
        object_list = Book.objects.all()
        return object_list


class DetailProductView(DetailView):
    """
    Class View untuk menampilkan halaman Detail produk yang dipilih (di klik)
    """
    model = Book
    template_name = "product/detail.html"
    context_object_name = "Books"
    extra_context = {}

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.query_pk_and_slug = True
        self.queryset = Book.objects.filter(id=kwargs.get("pk"))

        if request.method == "GET":

            self.extra_context.update({
                "page_title": Book.objects.get(id=kwargs.get("pk")).title,
            })

            print("Siapa user saat ini: {}".format(request.user))

        return super().get(request, self.query_pk_and_slug)


class PublisherListView(ListView):
    """
    Class View untuk menampilkan halaman Beranda penerbit buku.
    """
    model = Publisher
    context_object_name = "publisher"
    extra_context = {"page_title": "Daftar Penerbit", "website": "Toko Buku"}


class PublisherDetailView(DetailView):
    """
    Class View untuk menampilkan halaman Detail penerbit buku yang dipilih (di klik).
    """
    model = Publisher
    template_name = "product/publisher_detail.html"
    context_object_name = "publisher"
    extra_context = {}

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.query_pk_and_slug = True
        self.queryset = Publisher.objects.filter(id=kwargs.get("pk"))

        if request.method == "GET":

            self.extra_context.update({
                "page_title": Publisher.objects.get(id=kwargs.get("pk")).name,
                "related_book": Book.objects.filter(publisher_id=kwargs.get("pk")),
            })

        return super().get(request, *args, **kwargs)


class WriterListView(ListView):
    """
    Class View untuk menampilkan halaman Beranda penulis buku.
    """
    model = Writer
    context_object_name = "writer"
    extra_context = {"page_title": "Daftar Penulis", "website": "Toko Buku"}


class WriterDetailView(DetailView):
    """
    Class View untuk menampilkan halaman Detail penulis buku yang dipilih (di klik).
    """
    model = Writer
    template_name = "product/writer_detail.html"
    context_object_name = "writer"
    extra_context = {}

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.query_pk_and_slug = True
        self.queryset = Writer.objects.filter(id=kwargs.get("pk"))

        if request.method == "GET":

            self.extra_context.update({
                "page_title": Writer.objects.get(id=kwargs.get("pk")).name,
                "related_book": Book.objects.filter(writer_id=kwargs.get("pk")),
            })

        return super().get(request, *args, **kwargs)


class SearchResultView(ListView):
    """
    Class View untuk melakukan pencarian data.
    """
    model = Book
    template_name = "search.html"
    extra_context = {}

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get("q")

        object_list = Book.objects.filter(
            Q(title__icontains=query)
        )

        # Update context dengan kata kunci dari pencarian di HTML
        self.extra_context.update({"keyword": query})

        return object_list

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.queryset = self.get_queryset()
        not_found = len(self.queryset)

        if not_found == 0:
            self.extra_context.update({
                "message": "Tidak ditemukan."
            })

        # # Untuk melihat isi QuerySet melalui terminal/command prompt
        # print("Isi data QuerySet = {}".format(self.queryset))
        # print("Jumlah isi data QuerySet = {}".format(len(self.queryset)))

        return super().get(request, *args, **kwargs)
