# Generated by Django 4.2.2 on 2023-07-06 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_tarea_estado_alter_tarea_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='observaciones',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='prioridad',
            field=models.CharField(choices=[('baja', 'Baja'), ('media', 'Media'), ('máxima', 'Máxima')], max_length=10),
        ),
    ]
