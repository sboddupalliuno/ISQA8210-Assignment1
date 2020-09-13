from django.urls import path
from .views import (
    VehiclesownListView,
    VehiclesownUpdateView,
    VehiclesownDetailView,
    VehicleswonDeleteView,
    VehiclesownCreateView,
)


urlpatterns = [

    path('<int:pk>/edit/',
         VehiclesownUpdateView.as_view(), name='vehiclesown_edit'),
    path('<int:pk>/',
         VehiclesownDetailView.as_view(), name='vehiclesown_detail'),
    path('<int:pk>/delete/',
         VehicleswonDeleteView.as_view(), name='vehiclesown_delete'),

    path('', VehiclesownListView.as_view(), name='vehiclesown_list'),
    path('new/', VehiclesownCreateView.as_view(), name='vehiclesown_new'),


]
