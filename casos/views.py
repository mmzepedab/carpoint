from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from .models import Caso

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