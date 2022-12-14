# Generated by Django 3.2 on 2022-10-24 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0014_alter_materia_nombre'),
    ]

    operations = [
        migrations.CreateModel(
            name='VersionesHorario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('version', models.IntegerField(default=1)),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('status_model', models.BooleanField(default=True)),
                ('horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.horario')),
            ],
            options={
                'verbose_name': 'Version de horario',
                'verbose_name_plural': 'Versiones de horario',
                'ordering': ['activo'],
            },
        ),
        migrations.CreateModel(
            name='PeriodosHorario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo', models.BooleanField(default=True)),
                ('hora_inicio', models.TimeField()),
                ('hora_fin', models.TimeField()),
                ('status_model', models.BooleanField(default=True)),
                ('asignatura', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.asignatura')),
                ('version_horario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webapp.versioneshorario')),
            ],
            options={
                'verbose_name': 'Periodo de horario',
                'verbose_name_plural': 'Periodos de horario',
                'ordering': ['activo'],
            },
        ),
    ]
