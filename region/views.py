from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from .models import Province, City


# Create your views here.
class RegionListView(ListView):
    template_name = "region/city_list.html"
    model = City
    context_object_name = "Cities"
    extra_context = {"page_title": "Regional",
                     "website": "Toko Buku", }

    # def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
    #     return super().get(request, *args, **kwargs)
