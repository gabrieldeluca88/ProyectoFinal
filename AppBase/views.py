from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .models import *
from .forms import *

# Create your views here.
def inicio(request):
    try: 
        avatar = Avatar.objects.get(user=request.user.id)
        return render(request, 'inicio.html', {'url': avatar.imagen.url})
    except:
        return render(request, "inicio.html")
    
def AboutMe(request):
    return render(request, "aboutme.html")
    

@login_required   
def agregar_auto(request):
    if request.method == 'POST':
        mi_formulario = AutosForm(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            auto = Auto(modelo=request.POST['modelo'], fecha_salida=request.POST['fecha_salida'], tipo=request.POST['tipo'], marca=request.POST['marca'], descripcion=request.POST['descripcion'], valoracion=request.POST['valoracion'],)
            auto.save()
            return render(request, "inicio.html", {"mensaje": "Muy bien agregaste tu auto :D"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = AutosForm()
        return render(request, "agregar_auto.html", {"mi_formulario": mi_formulario})

@login_required  
def lista_autos(request):
    orden = request.GET.get('orden', None)
    autos = Auto.objects.all()
    if orden == 'lanzamiento':
        autos = autos.order_by('-fecha_salida')
    elif orden == 'valoracion':
        autos = autos.order_by('-valoracion')
    return render(request, "ver_autos.html", {"autos": autos})

@login_required
def eliminar_auto(request, id):
    if request.method == 'POST':
        auto = Auto.objects.get(id=id)
        auto.delete()
        auto = Auto.objects.all()
        return HttpResponseRedirect('/l-autos')

@login_required    
def editar_auto(request, id):
    auto = Auto.objects.get(id=id)
    if request.method == 'POST':
        mi_formulario = AutosForm(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            auto.modelo = data['modelo']
            auto.fecha_salida = data['fecha_salida']
            auto.tipo = data['tipo']
            auto.marca = data['marca']
            auto.descripcion = data['descripcion']
            auto.valoracion = data['valoracion']
            auto.save()
            return render(request, "inicio.html", {"mensaje": "Cambios realizados ;)"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = AutosForm(initial={
            "modelo": auto.modelo,
            "fecha_salida": auto.fecha_salida,
            "tipo": auto.tipo,
            "marca": auto.marca,
            "descripcion": auto.descripcion,
            "valoracion": auto.valoracion
        })
        return render(request, "editar_autos.html", {"mi_formulario": mi_formulario, "id": auto.id})

@login_required    
def agregar_resena(request):
    mi_formulario = ResenaForm()
    if request.method == 'POST':
        mi_formulario = ResenaForm(request.POST)
        if mi_formulario.is_valid():
            mi_formulario.save()
            return HttpResponseRedirect('/l-resenas')
    return render(request, 'agregar_resena.html', {'mi_formulario': mi_formulario})

@login_required
def lista_resenas(request):
    resenas = Resena.objects.all()
    return render(request, 'lista_resenas.html', {'reseñas': resenas})

@login_required
def eliminar_resena(request, id):
    if request.method == 'POST':
        resena = Resena.objects.get(id=id)
        resena.delete()
        resena = Resena.objects.all()
        return HttpResponseRedirect('/l-resenas')

login_required    
def editar_resena(request, id):
    resena = Resena.objects.get(id=id)
    if request.method == 'POST':
        mi_formulario = ResenaForm(request.POST)
        if mi_formulario.is_valid():
            data = mi_formulario.cleaned_data
            resena.autor = data['autor']
            resena.contenido = data['contenido']
            resena.auto = data['auto']
            resena.save()
            return render(request, "inicio.html", {"mensaje": "Cambios realizados ;)"})
        else:
            return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
    else:
        mi_formulario = ResenaForm(initial={
            "autor": resena.autor,
            "contenido": resena.contenido,
            "auto": resena.auto,
        })
        return render(request, "editar_resena.html", {"mi_formulario": mi_formulario, "id": resena.id})

@login_required
def busqueda_autos(request):
    return render(request, 'buscar_autos.html')

@login_required
def buscar_modelo(request):
    if request.method == 'GET':
        form = BuscarModelo(request.GET)
        if form.is_valid():
            modelo = form.cleaned_data['modelo']
            autos = Auto.objects.filter(modelo__icontains=modelo)
            return render(request, 'res_busqueda_modelo.html', {'autos': autos, 'modelo': modelo})
    else:
        form = BuscarModelo()
    return render(request, 'busq_modelo.html', {'form': form})

@login_required
def buscar_tipo(request):
    if request.method == 'GET':
        form = BuscarTipo(request.GET)
        if form.is_valid():
            tipo = form.cleaned_data['tipo']
            autos = Auto.objects.filter(tipo__icontains=tipo)
            return render(request, 'res_busqueda_tipo.html', {'autos': autos, 'tipo': tipo})
    else:
        form = BuscarTipo()
    return render(request, 'busq_tipo.html', {'form': form})

@login_required
def buscar_marca(request):
    if request.method == 'GET':
        form = BuscarMarca(request.GET)
        if form.is_valid():
            marca = form.cleaned_data['marca']
            autos = Auto.objects.filter(marca__icontains=marca)
            return render(request, 'res_busqueda_marca.html', {'autos': autos, 'marca': marca})
    else:
        form = BuscarMarca()
    return render(request, 'busq_marca.html', {'form': form})

@login_required
def buscar_valoracion(request):
    if request.method == 'GET':
        form = BuscarValoracion(request.GET)
        if form.is_valid():
            valoracion = form.cleaned_data['valoracion']
            autos = Auto.objects.filter(valoracion__icontains=valoracion)
            return render(request, 'res_busqueda_valoracion.html', {'autos': autos, 'valoracion': valoracion})
    else:
        form = BuscarValoracion()
    return render(request, 'busq_valoracion.html', {'form': form})


@login_required
def lista_temas(request):
    temas = Tema.objects.all()
    return render(request, 'foro.html', {'temas': temas})

@login_required
def crear_tema(request):
    if request.method == 'POST':
        form = TemaForm(request.POST)
        if form.is_valid():
            tema = form.save(commit=False)
            tema.creador = request.user
            tema.save()
            return HttpResponseRedirect('/foro')
    else:
        form = TemaForm()
    return render(request, 'crear_tema.html', {'form': form})

@login_required
def editar_tema(request, pk):
    tema = get_object_or_404(Tema, pk=pk)
    if request.method == 'POST':
        form = TemaForm(request.POST, instance=tema)
        if form.is_valid():
            tema = form.save()
            return HttpResponseRedirect('/foro')
    else:
        form = TemaForm(instance=tema)
    return render(request, 'editar_tema.html', {'form': form, 'tema': tema})

@login_required
def eliminar_tema(request, pk):
    tema = get_object_or_404(Tema, pk=pk)
    tema.delete()
    return HttpResponseRedirect('/foro')

@login_required
def detalle_tema(request, pk):
    tema = get_object_or_404(Tema, pk=pk)
    comentarios = Comentario.objects.filter(tema=tema)
    form = ComentarioForm()
    return render(request, 'detalle_tema.html', {'tema': tema, 'comentarios': comentarios, 'form': form})

@login_required
def crear_comentario(request, pk):
    tema = get_object_or_404(Tema, pk=pk)
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.creador = request.user
            comentario.tema = tema
            comentario.save()
            return HttpResponseRedirect(reverse('DetalleTema', args=[tema.pk]))
    else:
        form = ComentarioForm()
    return render(request, 'crear_comentario.html', {'form': form})
