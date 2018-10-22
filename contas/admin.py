from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
# Register your models here.

from .models import Usuario, Coordenador

class CoordenadorInline(admin.StackedInline):
    model = Coordenador
    can_delete = False
    verbose_name_plural = 'Coordenadores'
    fk_name = 'usuario'

class UsuarioCoordenadorAdmin(admin.ModelAdmin):
    model = Usuario
    inlines = (CoordenadorInline, )
    list_display = ('username', )
    list_filter = ('perfil',)
    filter_horizontal = ()
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username',)}
        ),
    )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UsuarioCoordenadorAdmin, self).get_inline_instances(request, obj)

admin.site.register(Usuario, UsuarioCoordenadorAdmin)
admin.site.unregister(Group)