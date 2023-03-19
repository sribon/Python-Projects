from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'store/home.html', context)

def modulos(request):
    context = {}
    return render(request, 'store/modulos.html', context)

def baterias(request):
    context = {}
    return render(request, 'store/baterias.html', context)

def fcarga(request):
    context = {}
    return render(request, 'store/fcarga.html', context)

def ffrontal(request):
    context = {}
    return render(request, 'store/ffrontal.html', context)

def camaras(request):
    context = {}
    return render(request, 'store/camaras.html', context)

def extra(request):
    context = {}
    return render(request, 'store/extra.html', context)