# Generated by Django 4.2.3 on 2023-07-14 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField(blank=True, null=True)),
                ('lugar', models.CharField(blank=True, db_comment='guarda la ubicacion de la cita ', max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, db_comment='guarda el nombre de quien cita ', max_length=45, null=True)),
            ],
            options={
                'db_table': 'agendamiento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoriaservicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
                ('precio', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'categoriaservicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Categoriataller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'categoriataller',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Contrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, db_comment='guarda los terminos y condiciones de cada contrato ', max_length=45, null=True)),
                ('nombre', models.CharField(blank=True, db_comment='guarda el nombre del contrato ', max_length=45, null=True)),
                ('persona_idpersona', models.IntegerField()),
            ],
            options={
                'db_table': 'contrato',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cuerpofacrura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.CharField(blank=True, max_length=45, null=True)),
                ('valorunitariol', models.IntegerField(blank=True, null=True)),
                ('valortotal', models.IntegerField(blank=True, null=True)),
                ('scripcion_idscripcion', models.IntegerField()),
            ],
            options={
                'db_table': 'cuerpofacrura',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('codigo', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'departamento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, db_comment='guarda el nombre de la empresa ', max_length=45, null=True)),
                ('direccion', models.CharField(blank=True, db_comment='guarda la direccion de la empresa ', max_length=45, null=True)),
                ('telefono', models.IntegerField(blank=True, db_comment='guarda el contacto de la empresa ', null=True)),
                ('correo', models.CharField(blank=True, db_comment='guarda el correo de la empresa ', max_length=45, null=True)),
                ('razonsocial', models.CharField(blank=True, db_comment='guarda el nombre juridico de la empresa', max_length=45, null=True)),
                ('catgtall_id', models.IntegerField()),
            ],
            options={
                'db_table': 'empresa',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Faccabeza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(blank=True, max_length=45, null=True)),
                ('fecha', models.DateField(blank=True, null=True)),
                ('valor_unitario', models.IntegerField(blank=True, db_column='valor unitario', null=True)),
                ('valortotal', models.IntegerField(blank=True, null=True)),
                ('pagos_tarjetacredito', models.IntegerField()),
            ],
            options={
                'db_table': 'faccabeza',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('ciudad_idciudad', models.IntegerField()),
            ],
            options={
                'db_table': 'municipio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Pagos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.FloatField(blank=True, null=True)),
                ('monto', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pagos',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'servicio',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tdocumento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
                ('abreviatura', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tdocumento',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Tpempresario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=45, null=True)),
                ('descripcion', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'tpempresario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('telefono', models.IntegerField(blank=True, null=True)),
                ('correo', models.CharField(blank=True, max_length=45, null=True)),
                ('contraseña', models.CharField(blank=True, max_length=45, null=True)),
                ('genero', models.CharField(blank=True, max_length=45, null=True)),
                ('fechanacimiento', models.DateField(blank=True, db_column='fechaNacimiento', null=True)),
            ],
            options={
                'db_table': 'usuario',
                'managed': False,
            },
        ),
    ]
