from django.shortcuts import render, redirect
from .models import Laboratorio, Visit
from django.contrib.auth.decorators import login_required

@login_required
def mostrar(request):
    laboratorios = Laboratorio.objects.all()
    user = request.user
    visit, created = Visit.objects.get_or_create(user=user)
    visit.visit_count += 1
    visit.save()
    visit_count = visit.visit_count
    return render(request, 'mostrar.html', {'laboratorios': laboratorios, 'visit_count': visit_count})

@login_required
def agregar(request):
    if request.method == "POST":
        nombre = request.POST['nombre']
        ciudad = request.POST['ciudad']
        pais = request.POST['pais']
        laboratorio = Laboratorio(nombre=nombre, ciudad=ciudad, pais=pais)
        laboratorio.save()
        return redirect('/')
    else:
        return render(request, 'agregar.html')

@login_required
def editar(request, id):
    lab = Laboratorio.objects.get(id=id)
    data = {
        'titulo': 'Editar laboratorio',
        'lab': lab
    }
    return render(request, "editar.html", data)

@login_required
def edit_labs(request):
    id = int(request.POST['id'])
    nombre = request.POST['nombre']
    ciudad = request.POST['ciudad']
    pais = request.POST['pais']

    lab = Laboratorio.objects.get(id=id)
    lab.nombre = nombre
    lab.ciudad = ciudad
    lab.pais = pais
    lab.save()

    return redirect('/')

@login_required
def eliminar(request, id):
    lab = Laboratorio.objects.get(id=id)
    lab.delete()
    return redirect('/')

@login_required
def inicio_test(request):
    return render(request, 'inicio_test.html')

@login_required
def visitas(request):
    user = request.user
    visit= Visit.objects.get(user=user)
    visit.visit_count += 1
    visit.save()
    visit_count = visit.visit_count
    laboratorios = Laboratorio.objects.all() 
    return render(request, 'mostrar.html', {'laboratorios': laboratorios, 'visit_count': visit_count})
