from django.contrib import admin
from .models import t_tareas


# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    readonly_fields = ("creado",)

admin.site.register(t_tareas,TaskAdmin)
