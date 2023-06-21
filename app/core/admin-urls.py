from django.urls import path

from .views import (
    ApplicationAdminCreateView,
    ApplicationAdminDetailUpdateView,
    ApplicationAdminListView,
)

urlpatterns = [
    path(
        "",
        ApplicationAdminListView.as_view(),
        name="application-admin-list",
    ),
    path("add/", ApplicationAdminCreateView.as_view(), name="application-admin-add"),
    path(
        "updates/<slug:slug>/",
        ApplicationAdminDetailUpdateView.as_view(),
        name="application-admin-detail-update",
    ),
]
