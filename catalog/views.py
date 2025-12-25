from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView, View

from catalog.models import Product

from .forms import ProductForm


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:dogs_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")


class ContactsView(View):
    def get(self, request):
        """Метод GET обрабатывает вывод контактной формы"""
        return render(request, "catalog/contacts.html")

    def post(self, request):
        """Метод POST обрабатывает отправленные данные"""
        name = request.POST.get("name")
        # Можно обработать данные, отправить письмо и т.п.
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
