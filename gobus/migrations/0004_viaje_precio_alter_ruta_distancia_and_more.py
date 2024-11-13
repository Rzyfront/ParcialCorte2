# Generated by Django 5.1.3 on 2024-11-13 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gobus', '0003_remove_boleto_fecha_viaje_remove_boleto_hora_salida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='viaje',
            name='precio',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ruta',
            name='distancia',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='ruta',
            name='duracion_estimada',
            field=models.CharField(max_length=20),
        ),
    ]
