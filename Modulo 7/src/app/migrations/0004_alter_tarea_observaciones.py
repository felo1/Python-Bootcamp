# Generated by Django 4.2.2 on 2023-07-06 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_tarea_observaciones_alter_tarea_prioridad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarea',
            name='observaciones',
            field=models.CharField(blank=True, max_length=1024, null=True),
        ),
    ]
