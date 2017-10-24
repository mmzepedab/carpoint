from django.shortcuts import render

from .models import Caso

# Create your views here.


def caso_list(request):
    casos = Caso.objects.all()

    context = {
        "casos" : casos,
    }

    return render(request, "caso/caso_list.html",  context)