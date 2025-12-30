from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
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


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        dog = form.save()
        user = self.request.user
        dog.owner = user
        dog.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if obj.owner != self.request.user and not self.request.user.has_perm("catalog.can_unpublish_product"):
            raise PermissionDenied("Вы не владелец данного продукта и не можете его редактировать.")
        return obj

    def form_valid(self, form):
        product = form.save(commit=False)

        # Проверяем, имеет ли пользователь разрешение изменять статус публикации
        if "is_publication" in form.changed_data and not self.request.user.has_perm("catalog.can_unpublish_product"):
            raise PermissionDenied("Вы не имеете прав менять статус публикации продукта.")

        product.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy("catalog:product_list")
    permission_required = "catalog.delete_product"

    def dispatch(self, request, *args, **kwargs):
        """
        Переопределяем метод dispatch(), чтобы провести дополнительные проверки
        перед удалением продукта.
        """
        obj = self.get_object()
        if obj.owner != self.request.user and not self.request.user.has_perm("catalog.delete_product"):
            raise PermissionDenied("Только владельцы и модераторы могут удалить продукт.")
        return super().dispatch(request, *args, **kwargs)


class ContactsView(View):
    def get(self, request):
        """Метод GET обрабатывает вывод контактной формы"""
        return render(request, "catalog/contacts.html")

    def post(self, request):
        """Метод POST обрабатывает отправленные данные"""
        name = request.POST.get("name")
        # Можно обработать данные, отправить письмо и т.п.
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
