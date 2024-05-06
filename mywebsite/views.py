from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView
from product.models import Book
from typing import Any


class IndexHomePagesViews(ListView):
    model = Book
    template_name = "index.html"
    context_object_name = "Books"
    extra_context = {
        "page_title": "Beranda",
        "website": "Toko Buku",
    }
    paginate_by = 12

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        self.queryset = Book.objects.all()
        return super().get(request, *args, **kwargs)
