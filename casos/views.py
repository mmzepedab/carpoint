# -*- coding: 850 -*-
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Caso, Avance

# Create your views here.

@login_required(login_url='/account/login/')
def caso_list(request):
    if request.user.is_authenticated():
        logged_in_user = request.user
        logged_in_user_casos = Caso.objects.filter(cliente=logged_in_user)
    else:
        logged_in_user_casos = ""

    context = {
        "casos" : logged_in_user_casos,
    }

    return render(request, "caso/caso_list.html",  context)

@login_required(login_url='/account/login/')
def caso_detail(request, caso_id):
    if request.user.is_authenticated():
        logged_in_user = request.user
        logged_in_user_casos = Caso.objects.filter(cliente=logged_in_user)
    else:
        logged_in_user_casos = ""

    caso = get_object_or_404(Caso, pk=caso_id)
    avances = Avance.objects.all().filter(caso=caso).values(
        'pk',
        'fecha_creado',
        'descripcion',
        'imagen_1',
        'imagen_2',
        'imagen_3',
        'imagen_4',
        'imagen_5',
    )

    context = {
        "caso" : caso,
        "avances" : avances
    }

    return render(request, "caso/caso_detail.html",  context)