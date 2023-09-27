from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.utils import timezone
from .formularios import f_creatareas
from .models import t_tareas

# Create your views here.
def v_home(request):
    return render(request, 'home.html')

def v_signeup(request):
    if request.method == 'GET':
        return render(request, 'signup.html',{
            'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                l_user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'])
                l_user.save()
                login(request, l_user)
                return redirect('u_tareas')
            except IntegrityError:
                return render(request, 'signup.html',{
                    'form': UserCreationForm,
                    "error":'Usuario ya existe'
                })
        return render(request, 'signup.html',{
            'form': UserCreationForm,
            "error":'Pasword incorrecto'
        })
       
@login_required
def v_tareas(request):
       l_tareas = t_tareas.objects.filter(usuario=request.user, completado__isnull=True)
       return render(request, 'tareas.html', {'p_tareas':l_tareas})

@login_required
def v_tareascompletadas(request):
       l_tareas = t_tareas.objects.filter(usuario=request.user, completado__isnull=False).order_by('-completado')
       return render(request, 'tareas.html', {'p_tareas':l_tareas})

@login_required
def v_tareacompleta(request, p_id):
        l_tarea = get_object_or_404(t_tareas, pk=p_id, usuario=request.user)
        if request.method == 'POST':
             l_tarea.completado = timezone.now()
             l_tarea.save()
             return redirect('u_tareas')

@login_required
def v_tareaelimina(request, p_id):
        l_tarea = get_object_or_404(t_tareas, pk=p_id, usuario=request.user)
        if request.method == 'POST':
             l_tarea.delete()
             return redirect('u_tareas')

@login_required
def v_tareasdetalle(request, p_id):
        if request.method == 'GET':
            l_tarea = get_object_or_404(t_tareas, pk=p_id, usuario=request.user)
            l_form = f_creatareas(instance=l_tarea)
            return render(request, 'tareas_detalle.html', {'p_tarea':l_tarea, 'p_form':l_form})
        else:
            try:
                l_tarea = get_object_or_404(t_tareas, pk=p_id, usuario=request.user)
                l_form = f_creatareas(request.POST, instance=l_tarea)
                l_form.save()
                return redirect('u_tareas')
            except ValueError:
                return render(request, 'tareas_detalle.html', {'p_tarea':l_tarea, 'p_form':l_form,
                'p_error': 'Error actualizando tarea'})
                 

@login_required
def v_creatareas(request):
        if request.method == 'GET':
            return render(request, 'crear_tarea.html', {
                    'form': f_creatareas
            })
        else:
            try:
                form = f_creatareas(request.POST)
                nueva_tarea = form.save(commit=False)
                nueva_tarea.usuario = request.user
                nueva_tarea.save()
                return redirect('u_tareas')
            except ValueError:
                return render(request, 'crear_tarea.html', {
                    'form': f_creatareas,
                    'error': 'Digite datos validos por favor'
                })
                 

@login_required
def v_logout(request):
    logout(request),
    return redirect('u_home')

def v_signin(request):
        if request.method == 'GET':
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
            })
        else:
            l_user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
            if l_user is None:
                return render(request, 'signin.html', {
                    'form': AuthenticationForm,
                    "error":'Usuario y/o clave incorrecto'
                })
            else:
                login(request, l_user)
                return redirect('u_tareas')

        


