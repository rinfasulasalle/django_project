from django.db import models

class Usuario(models.Model):
    id = models.CharField(primary_key=True, max_length=20, unique=True)
    usuario_rol = models.CharField(max_length=20, choices=[
        ('Administrador', 'Administrador'),
        ('Recursos Humanos', 'Recursos Humanos'),
        ('Trabajador', 'Trabajador'),
        ('Sin acceso', 'Sin acceso')
    ], default='Sin acceso')
    usuario_nombres = models.CharField(max_length=100)
    usuario_apellidos = models.CharField(max_length=100)
    usuario_correo = models.EmailField(max_length=100, unique=True)
    usuario_contrasenia = models.CharField(max_length=50)
    usuario_sexo = models.CharField(max_length=20, choices=[
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
        ('No Especificado', 'No Especificado')
    ], default='No Especificado')
    usuario_telefono = models.CharField(max_length=50)

    def __str__(self):
        return self.id

class Trabajador(models.Model):
    trabajador_id = models.CharField(primary_key=True, max_length=20, unique=True)
    trabajador_fecha_nacimiento = models.DateField()
    trabajador_tipo_documento = models.CharField(max_length=50)
    trabajador_path_documento = models.CharField(max_length=255, default='PATH/noNe')
    trabajador_nacionalidad = models.CharField(max_length=50, default='No Especificado')
    trabajador_ubigeo = models.CharField(max_length=255, default='No Especificado')
    trabajador_estado_civil = models.CharField(max_length=20, choices=[
        ('Soltero', 'Soltero'),
        ('Casado', 'Casado'),
        ('Viudo', 'Viudo'),
        ('Divorciado', 'Divorciado'),
        ('Conviviente', 'Conviviente'),
        ('No Especificado', 'No Especificado')
    ], default='No Especificado')
    trabajador_path_doc_estado_civil = models.CharField(max_length=255, default='PATH/noNe')
    trabajador_fecha_ingreso = models.DateField()
    trabajador_fecha_ingreso_sistema = models.DateField()
    trabajador_edad = models.IntegerField()
    trabajador_record = models.DecimalField(max_digits=20, decimal_places=2)
    trabajador_exp_previa = models.DecimalField(max_digits=20, decimal_places=2)
    trabajador_total_anios_exp = models.DecimalField(max_digits=20, decimal_places=2)

    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)  # Relación uno a uno con Usuario

    def __str__(self):
        return self.trabajador_id

class Sueldo(models.Model):
    id_trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE, primary_key=True)
    sueldo_valor_basico = models.DecimalField(max_digits=20, decimal_places=2)
    sueldo_asigfam_porcentaje = models.DecimalField(max_digits=20, decimal_places=2)
    sueldo_asignacion_familiar = models.DecimalField(max_digits=20, decimal_places=2)
    sueldo_bono_porcentaje = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    sueldo_monto_bono = models.DecimalField(max_digits=20, decimal_places=2)
    sueldo_mensual = models.DecimalField(max_digits=20, decimal_places=2)
    sueldo_anual = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return str(self.id_trabajador)

class Contrato(models.Model):
    id_trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE, primary_key=True)
    contrato_tipo = models.CharField(max_length=255)
    contrato_opcion = models.CharField(max_length=255)
    empleo_tipo = models.CharField(max_length=50)
    empleo_situacion = models.CharField(max_length=50)
    empleo_area = models.CharField(max_length=50)
    empleo_proyecto = models.CharField(max_length=50)
    empleo_departamento = models.CharField(max_length=50)
    empleo_cargo = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id_trabajador)

class CuentaBancaria(models.Model):
    id_trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE, primary_key=True)
    cuenta_bancaria_codigo_cci = models.CharField(max_length=255, unique=True)
    cuenta_bancaria_codigo = models.CharField(max_length=255, unique=True)
    cuenta_bancaria_banco = models.CharField(max_length=255)
    cuenta_bancaria_tipo = models.CharField(max_length=20, choices=[
        ('Sueldo', 'Sueldo'),
        ('CTS', 'CTS')
    ])

    def __str__(self):
        return str(self.id_trabajador)

class Direccion(models.Model):
    id_trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE, primary_key=True)
    direccion_pais = models.CharField(max_length=255)
    direccion_departamento = models.CharField(max_length=255)
    direccion_provincia = models.CharField(max_length=255)
    direccion_distrito = models.CharField(max_length=255)
    direccion_detalle = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id_trabajador)

class Estudio(models.Model):
    id_trabajador = models.OneToOneField(Trabajador, on_delete=models.CASCADE, primary_key=True)
    estudio_nivel_educativo = models.CharField(max_length=255)
    estudio_situacion_especial = models.CharField(max_length=255, default='Situación especial no especificada')
    estudio_regimen_laboral = models.CharField(max_length=255, default='Régimen laboral no especificado')
    estudio_regimen_laboral_aseguramiento = models.CharField(max_length=255, default='Aseguramiento no especificado')
    estudio_institucion = models.CharField(max_length=255, default='Institución no especificada')
    estudio_carrera_educativa = models.CharField(max_length=255, default='Carrera no especificada')
    estudio_capacitacion = models.CharField(max_length=255, default='Capacitación no especificada')
    estudio_especializacion = models.CharField(max_length=255, default='Especialización no especificada')
    estudio_id_colegiatura = models.CharField(max_length=255, default='No especificado')
    estudio_fecha_colegiatura = models.DateField(default='1212-12-12')
    estudio_sede_colegiatura = models.CharField(max_length=255, default='Sede colegiatura no especificada')
    estudio_condicion = models.CharField(max_length=20, choices=[
        ('Habilitado', 'Habilitado'),
        ('No habilitado', 'No habilitado'),
        ('No especificado', 'No especificado')
    ], default='No especificado')

    def __str__(self):
        return str(self.id_trabajador)
