from django.urls import path
from .views import IndexProductView, DetailProductView, SearchResultView


app_name = "product"

urlpatterns = [
    path('', IndexProductView.as_view(), name="index"),
    path('search/', SearchResultView.as_view(), name="search_result"),
    path('books/<int:pk>/<slug:slug>',
         DetailProductView.as_view(), name="product-detail"),
]
