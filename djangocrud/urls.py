"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
/*Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tareas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.v_home, name="u_home"),
    path('signup/', views.v_signeup, name="u_signup"),
    path('tareas/', views.v_tareas, name="u_tareas"),
    path('tareas/completadas', views.v_tareascompletadas, name="u_tareascompletadas"),
    path('crear_tarea/', views.v_creatareas, name="U_creartarea"),
    path('tareas/<int:p_id>', views.v_tareasdetalle, name="u_tareasdetalle"),
    path('tareas/<int:p_id>/completa', views.v_tareacompleta, name="u_tareacompleta"),
    path('tareas/<int:p_id>/elimina', views.v_tareaelimina, name="u_tareaelimina"),
    path('logout/', views.v_logout, name="u_logout"),
    path('signin/', views.v_signin, name="u_signin"),
]
