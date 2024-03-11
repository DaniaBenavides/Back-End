from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    my_context = {'interes1':'Ver películas y series', 'interes2':'Danza folklorika', 'interes3':'Grupo Cadena'}

    return render(request, 'App/index.html', context = my_context)
    #return HttpResponse("Clase de Programación Back End")