# Generated by Django 3.2.4 on 2021-06-18 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutoriales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(default='Sin titulo', max_length=20)),
                ('detalle', models.CharField(default='Sin detalle', max_length=20)),
                ('publicado', models.BooleanField(default=False)),
            ],
        ),
    ]
