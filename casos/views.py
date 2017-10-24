from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Caso

# Create your views here.

@login_required(login_url='/account/login/')
def caso_list(request):
    casos = Caso.objects.all()

    context = {
        "casos" : casos,
    }

    return render(request, "caso/caso_list.html",  context)