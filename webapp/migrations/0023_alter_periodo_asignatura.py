# Generated by Django 3.2 on 2022-10-25 23:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0022_alter_periodo_asignatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='periodo',
            name='asignatura',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.asignatura'),
        ),
    ]
