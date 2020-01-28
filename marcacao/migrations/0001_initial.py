# Generated by Django 3.0.2 on 2020-01-26 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profissional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marcacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_cadastro', models.DateTimeField(auto_created=True)),
                ('id_profissional', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='profissional.Profissional')),
            ],
        ),
    ]