# Generated by Django 3.0.1 on 2019-12-28 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clinica_profissional', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorarioAgenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dia_semana', models.CharField(choices=[('Segunda', 'Segunda'), ('Terca', 'Terca'), ('Terca', 'Terca'), ('Quarta', 'Quarta'), ('Quinta', 'Quinta'), ('Sexta', 'Sexta'), ('Sabado', 'Sabado'), ('Domingo', 'Domingo')], max_length=20)),
                ('hora_inicial', models.TimeField()),
                ('hora_final', models.TimeField()),
                ('duracao', models.PositiveIntegerField()),
                ('ativado', models.BooleanField(default=True)),
                ('obs', models.TextField(blank=True, max_length=300, null=True)),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('id_clinica_profi', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='clinica_profissional.ClinicaProfissional')),
            ],
        ),
    ]
