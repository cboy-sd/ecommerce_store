# Generated by Django 4.0.4 on 2022-05-14 15:35

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='product',
            managers=[
                ('products', django.db.models.manager.Manager()),
            ],
        ),
    ]