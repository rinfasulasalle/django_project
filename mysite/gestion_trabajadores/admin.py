from django.contrib import admin
from .models import Usuario, Trabajador, Sueldo, Contrato, CuentaBancaria, Direccion, Estudio

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario_rol', 'usuario_nombres', 'usuario_apellidos', 'usuario_correo', 'usuario_sexo', 'usuario_telefono')
admin.site.register(Usuario, UsuarioAdmin)

class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ('trabajador_id', 'trabajador_fecha_nacimiento', 'trabajador_tipo_documento', 'trabajador_estado_civil', 'trabajador_fecha_ingreso')
admin.site.register(Trabajador, TrabajadorAdmin)

class SueldoAdmin(admin.ModelAdmin):
    list_display = ('id_trabajador', 'sueldo_valor_basico', 'sueldo_asigfam_porcentaje', 'sueldo_mensual', 'sueldo_anual')
admin.site.register(Sueldo, SueldoAdmin)

class ContratoAdmin(admin.ModelAdmin):
    list_display = ('id_trabajador', 'contrato_tipo', 'contrato_opcion', 'empleo_tipo', 'empleo_situacion', 'empleo_area', 'empleo_proyecto', 'empleo_departamento', 'empleo_cargo')
admin.site.register(Contrato, ContratoAdmin)

class CuentaBancariaAdmin(admin.ModelAdmin):
    list_display = ('id_trabajador', 'cuenta_bancaria_codigo_cci', 'cuenta_bancaria_codigo', 'cuenta_bancaria_banco', 'cuenta_bancaria_tipo')
admin.site.register(CuentaBancaria, CuentaBancariaAdmin)

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('id_trabajador', 'direccion_pais', 'direccion_departamento', 'direccion_provincia', 'direccion_distrito', 'direccion_detalle')
admin.site.register(Direccion, DireccionAdmin)

class EstudioAdmin(admin.ModelAdmin):
    list_display = ('id_trabajador', 'estudio_nivel_educativo', 'estudio_situacion_especial', 'estudio_regimen_laboral', 'estudio_regimen_laboral_aseguramiento', 'estudio_institucion', 'estudio_carrera_educativa', 'estudio_capacitacion', 'estudio_especializacion', 'estudio_id_colegiatura', 'estudio_fecha_colegiatura', 'estudio_condicion')
admin.site.register(Estudio, EstudioAdmin)
