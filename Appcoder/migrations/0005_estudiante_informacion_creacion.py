# Generated by Django 4.0.4 on 2022-05-26 05:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Appcoder', '0004_estudiante_tarjeta_presentacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='informacion_creacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
