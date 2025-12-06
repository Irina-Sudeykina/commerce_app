from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from catalog.models import Product


class ProductListView(ListView):
    model = Product


class ProducDetailView(DetailView):
    model = Product


class ContactsView(View):
    def get(self, request):
        """Метод GET обрабатывает вывод контактной формы"""
        return render(request, 'catalog/contacts.html')

    def post(self, request):
        """Метод POST обрабатывает отправленные данные"""
        name = request.POST.get('name')
        message = request.POST.get('message')
        # Можно обработать данные, отправить письмо и т.п.
        return HttpResponse(f"Спасибо, {name}! Ваше сообщение получено.")
