# -*- coding: 850 -*-
from django.shortcuts import render

from django.shortcuts import render, get_object_or_404

from django.contrib.auth.decorators import login_required

from .models import Caso, Avance, UsuarioAseguradora

import logging

# Get an instance of a logger
logger = logging.getLogger(__name__)
import sys
# Create your views here.

@login_required(login_url='/account/login/')
def caso_list(request):
    if request.user.is_authenticated():
        logged_in_user = request.user
        usuario_aseguradora = UsuarioAseguradora.objects.filter(usuario=logged_in_user).first()

        #print(usuario_aseguradora, file=sys.stderr)
        if usuario_aseguradora:
            is_aseguradora = True
            query = request.GET.get('search', '')
            logged_in_user_casos = Caso.objects.all().filter(aseguradora=usuario_aseguradora.aseguradora, cliente__username__icontains=query)
        else:
            is_aseguradora = False
            logged_in_user_casos = Caso.objects.filter(cliente=logged_in_user)
    else:
        logged_in_user_casos = ""

    context = {
        "casos" : logged_in_user_casos,
        "is_aseguradora": is_aseguradora,
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