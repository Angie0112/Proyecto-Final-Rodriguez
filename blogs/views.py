from django.shortcuts import render
from django.http import HttpResponse
from .models import Articulo
from django.template import loader

from django.views.generic import ListView
# Create your views here.


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def listar_articulos(request):
    contexto = { "articulos": Articulo.objects.all(), }
    http_response = render(
        request=request,
        template_name='blogs/lista_articulos.html',
        context=contexto,
    )
    return http_response


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)