from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import VehicleOwned
from django.urls import reverse_lazy

class VehiclesownListView(ListView):
    model = VehicleOwned
    template_name = 'vehiclesown_list.html'

class VehiclesownDetailView(DetailView):
    model = VehicleOwned
    template_name = 'vehiclesown_detail.html'
    login_url = 'login'

class VehiclesownUpdateView(UpdateView):
    model = VehicleOwned
    fields = ('make', 'model', 'VIN_number', 'date_of_purchase', 'date_of_last_service')
    template_name = 'vehiclesown_edit.html'
    success_url = reverse_lazy('vehiclesown_list')

class VehicleswonDeleteView(DeleteView):
    model = VehicleOwned
    template_name = 'vehiclesown_delete.html'
    success_url = reverse_lazy('vehiclesown_list')

class VehiclesownCreateView(CreateView):
    model = VehicleOwned
    template_name = 'vehiclesown.html'
    fields = ('make', 'model', 'VIN_number', 'date_of_purchase', 'date_of_last_service')
    success_url = reverse_lazy('vehiclesown_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

