from django.urls import path

from .views import ApplicationGetUpdateView, ApplicationListView

urlpatterns = [
    path("", ApplicationListView.as_view(), name="application-list"),
    path(
        "get-updates/<slug:slug>/",
        ApplicationGetUpdateView.as_view(),
        name="application-get-update",
    ),
]
