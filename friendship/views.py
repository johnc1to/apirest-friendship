from django.shortcuts import render

from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View        
from .models import Categoria, Incidentes, Centros
import json

""" Usuario """
from rest_framework import viewsets
from django.contrib.auth.models import User
from .serializers import UserSerializer

class CategoriaView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0): 
        if(id>0):
            categoria = list(Categoria.objects.filter(id=id).values())
            if len(categoria)>0:
                category= categoria[0]
                datos = {'message':'success', 'categoria':category}
            else:
                datos = {'message':'categoria not found...'}
            return JsonResponse(datos)
        else:
            categoria = list(Categoria.objects.values())  
            if len(categoria) > 0:
                datos  ={'message':'success', 'categoria':categoria}
            else: 
                datos = {'message':'categoria not found...'}
            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Categoria.objects.create(
            nombre=jd['nombre'],
        )
        datos = {'message':'success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        categoria = list(Categoria.objects.filter(id=id).values())
        if len(categoria)>0:
            category = Categoria.objects.get(id=id)
            category.nombre = jd['nombre']
            category.save()
            datos = {'message':'success'}
        
        else:
            datos = {'message':'categoria not found...'}
        return JsonResponse(datos)
    def delete(self, request, id):
        categoria = list(Categoria.objects.filter(id=id).values())
        if len(categoria)>0:
            Categoria.objects.filter(id=id).delete()
            datos = {'message':'success'}
        else:
            datos = {'message':'categoria not found...'}
        return JsonResponse(datos)

class IncidentesView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0): 
        if(id>0):
            incidente = list(Incidentes.objects.filter(id=id).values())
            if len(incidente)>0:
                incident = incidente[0]
                datos = {'message':'success', 'incidente':incident}
            else:
                datos = {'message':'incidente not found...'}
            return JsonResponse(datos)
        else:
            incidente = list(Incidentes.objects.values())  
            if len(incidente) > 0:
                datos  ={'message':'success', 'incidente':incidente}
            else: 
                datos = {'message':'incidente not found...'}

            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        #print(jd)
        Incidentes.objects.create(
                categoria_id = jd['categoria_id'],
                nombre=jd['nombre'],
                apellido = jd['apellido'],
                img = jd['img'] ,
                longitud = jd['longitud'],
                latitud = jd['latitud'] ,
        )
        datos = {'message':'success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        incidente = list(Incidentes.objects.filter(id=id).values())
        if len(incidente)>0:
            incident= Incidentes.objects.filter(id=id)
            incident.update(
                categoria_id = jd['categoria_id'],
                nombre=jd['nombre'],
                apellido = jd['apellido'],
                img = jd['img'] ,
                longitud = jd['longitud'],
                latitud = jd['latitud'] ,
            )
            datos = {'message':'success'}
        else:
            datos = {'message':'incidente not found...'}
        return JsonResponse(datos)
    def delete(self, request, id):
        incidente = list(Incidentes.objects.filter(id=id).values())
        if len(incidente)>0:
            Incidentes.objects.filter(id=id).delete()
            datos = {'message':'success'}
        else:
            datos = {'message':'incidente not found...'}
        return JsonResponse(datos)


class CentrosView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, id=0): 
        if(id>0):
            centro = list(Centros.objects.filter(id=id).values())
            if len(centro)>0:
                cent = centro[0]
                datos = {'message':'success', 'centro':cent}
            else:
                datos = {'message':'centro not found...'}
            return JsonResponse(datos)
        else:
            centro = list(Centros.objects.values())  
            if len(centro) > 0:
                datos  ={'message':'success', 'centro':centro}
            else: 
                datos = {'message':'centro not found...'}

            return JsonResponse(datos)

    def post(self, request):
        #print(request.body)
        jd=json.loads(request.body)
        Centros.objects.create(
                nombre = jd['nombre'], 
                telefono = jd['telefono'],
                img = jd['img'] ,
                latitud = jd['latitud'],
                longitud = jd['longitud'],
        )
        datos = {'message':'success'}
        return JsonResponse(datos)

    def put(self, request, id):
        jd = json.loads(request.body)
        centro = list(Centros.objects.filter(id=id).values())
        if len(centro)>0:
            cent = Centros.objects.filter(id=id)
            cent.update(
                nombre = jd['nombre'], 
                telefono = jd['telefono'],
                img = jd['img'] ,
                latitud = jd['latitud'],
                longitud = jd['longitud'],
            )
            datos = {'message':'success'}
        else:
            datos = {'message':'centro not found...'}
        return JsonResponse(datos)
    def delete(self, request, id):
        centro = list(Centros.objects.filter(id=id).values())
        if len(centro)>0:
            Centros.objects.filter(id=id).delete()
            datos = {'message':'success'}
        else:
            datos = {'message':'centro not found...'}
        return JsonResponse(datos)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer