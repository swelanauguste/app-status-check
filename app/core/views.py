from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView

from .models import Application


class ApplicationGetUpdateView(UpdateView):
    model = Application
    template_name = 'core/public/application_public_form.html'
    success_url = "/"
    fields = ["get_email_updates", "email"]


class ApplicationListView(ListView):
    model = Application
    template_name = 'core/public/application_public_list.html'
    

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Application.objects.filter(
                Q(application_number__iexact=query)
                | Q(nic_number__iexact=query)
                | Q(receipt_number__iexact=query)
            ).distinct()
        else:
            return Application.objects.none()


class ApplicationAdminDetailUpdateView(LoginRequiredMixin, UpdateView):
    model = Application
    template_name = 'core/admin/application_admin_form.html'
    success_url = "/"
    fields = ["application_number", "nic_number", "receipt_number", "status", "details"]


class ApplicationAdminCreateView(LoginRequiredMixin, CreateView):
    model = Application
    template_name = 'core/admin/application_admin_form.html'
    success_url = "/"
    fields = ["application_number", "nic_number", "receipt_number", "status", "details"]


class ApplicationAdminListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'core/admin/application_admin_list.html'

    def get_queryset(self):
        query = self.request.GET.get("admin-q")
        if query:
            return Application.objects.filter(
                Q(application_number__iexact=query)
                | Q(nic_number__iexact=query)
                | Q(receipt_number__iexact=query)
            ).distinct()
        else:
            return Application.objects.all()
