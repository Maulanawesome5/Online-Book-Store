from django.urls import path
from .views import RegionListView

app_name = "region"

urlpatterns = [
    path('', RegionListView.as_view(), name="index"),
]
