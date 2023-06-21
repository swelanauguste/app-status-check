from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("core.urls")),
    path("immigration-admin/", include("core.admin-urls")),
    path("admin/", admin.site.urls),
]
