# Generated by Django 4.2.7 on 2023-11-26 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_articulo_autor'),
        ('perfiles', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]