from django.urls import path
from .views import CategoriaView, IncidentesView, CentrosView

from django.conf.urls import include
from rest_framework import routers

from .views import UserViewSet
router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    
    path('', include(router.urls)),
    path('categorias/', CategoriaView.as_view(), name='categoria_list'),
    path('categorias/<int:id>', CategoriaView.as_view(), name='categoria_process'),
    path('incidentes/', IncidentesView.as_view(), name='product_list'),
    path('incidentes/<int:id>', IncidentesView.as_view(), name='product_process'),
    path('centros/', CentrosView.as_view(), name='centro_list'),
    path('centros/<int:id>', CentrosView.as_view(), name='centro_process'),
]