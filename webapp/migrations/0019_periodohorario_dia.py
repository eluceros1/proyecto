# Generated by Django 3.2 on 2022-10-24 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0018_rename_periodoshorario_periodohorario'),
    ]

    operations = [
        migrations.AddField(
            model_name='periodohorario',
            name='dia',
            field=models.CharField(default='lunes', max_length=10),
        ),
    ]
