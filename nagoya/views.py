from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import restaurant
from django.urls import reverse_lazy


class TopView(TemplateView):
    template_name = "top.html"

class ProductListView(ListView):
    model = restaurant
    template_name = "list.html"

class ProductCreateView(CreateView):
    model = restaurant
    fields = '__all__'

class ProductUpdateView(UpdateView):
    model = restaurant
    fields = '__all__'
    template_name_suffix = '_update_form'

class ProductDeleteView(DeleteView):
    model = restaurant
    template_name = "nagoya/restaurant_confirm_delete.html"
    success_url = reverse_lazy('list')