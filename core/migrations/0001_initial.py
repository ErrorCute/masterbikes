# Generated by Django 4.2.1 on 2023-06-20 01:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bicicleta',
            fields=[
                ('id_bicileta', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=30)),
                ('disponible', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('rut', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('numeroTelefono', models.IntegerField()),
                ('correo', models.EmailField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('usuario', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('clave', models.CharField(max_length=100)),
                ('rut', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='SolicitudArriendo',
            fields=[
                ('id_arriendo', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_arriendo', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('estado', models.BooleanField(default=False)),
                ('bicicleta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.bicicleta')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('nro_orden', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('id_detalle', models.CharField(max_length=150)),
                ('cod_producto', models.CharField(max_length=16)),
                ('fecha_compra', models.DateField()),
                ('fecha_despacho', models.DateField()),
                ('fecha_entrega', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
        ),
    ]
