from django.contrib import admin
from django.urls import path, include
from product.views import (PublisherListView, PublisherDetailView,
                           WriterListView, WriterDetailView)
from .views import IndexHomePagesViews


urlpatterns = [
    path('', IndexHomePagesViews.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('accounts/', include("django.contrib.auth.urls")),
    path('product/', include("product.urls", namespace="product")),
    path('publishers/', PublisherListView.as_view(), name="publisher"),
    path('publishers/<int:pk>/<slug:slug>', PublisherDetailView.as_view(),
         name="publisher-detail"),
    path('region/', include("region.urls", namespace="region")),
    #     path('tutorial/', include("tutorial.urls", namespace="tutorial")),
    path('writer/', WriterListView.as_view(), name="writer"),
    path('writer/<int:pk>/<slug:slug>',
         WriterDetailView.as_view(), name="writer-detail"),
]
