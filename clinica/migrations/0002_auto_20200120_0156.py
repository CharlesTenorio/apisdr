# Generated by Django 3.0.1 on 2020-01-20 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clinica',
            options={'ordering': ('nome', 'email')},
        ),
    ]
