# Generated by Django 5.1.5 on 2025-01-27 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='categorias',
            new_name='categoria',
        ),
    ]
