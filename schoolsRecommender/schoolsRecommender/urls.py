from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("schools/", include("schools.urls")),
    path("admin/", admin.site.urls),
]