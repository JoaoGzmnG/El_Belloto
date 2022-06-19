from django.shortcuts import render
from django.http import HttpResponse
from .models import Pendiente
from django.template import loader
from .forms import PendienteForm
from django.shortcuts import redirect

#FORMA SUGERIDA POR TUTORIAL DE DJANGO PROJECT
'''
def index(request):
    todo_list = Pendiente.objects.order_by('-pub_date')[:5]
    template = loader.get_template('app1/index.html')
    context = {
        'todo_list': todo_list,
    }
    return HttpResponse(template.render(context, request))
'''
#FORMA QUE CONOZCO
def index(request):
    return render(request, "app1/index.html") #app1 es la carpeta dentro de templates.
'''
def pendientes(request):
    return render(request, "app1/form_pendientes.html") #app1 es la carpeta dentro de templates.
'''
def empresas(request):
    return render(request, "app1/form_empresas.html") #app1 es la carpeta dentro de templates.

def sobre_mi(request):
    return render(request, "app1/sobre_mi.html") #app1 es la carpeta dentro de templates.

def pendientes_post(request):
    if request.method == 'POST':
        form = PendienteForm(data = request.POST)
        if form.is_valid():
            pendiente = form.save(commit = False)
            pendiente.save()
        else:
            print('Formulario no valido')
        return redirect('pendientes_post')
    else:
        form = PendienteForm()
        return render(request, 'app1/form_pendientes.html', {"form":form})