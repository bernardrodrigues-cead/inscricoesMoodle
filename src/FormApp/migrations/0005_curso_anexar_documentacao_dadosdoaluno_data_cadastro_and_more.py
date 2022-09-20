# Generated by Django 4.1.1 on 2022-09-20 18:57

import FormApp.validators
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0004_curso_nome_breve'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='anexar_documentacao',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dadosdoaluno',
            name='data_cadastro',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 9, 20, 18, 56, 59, 273932, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dadosdoaluno',
            name='documentacao',
            field=models.FileField(default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='dadosdoaluno',
            name='cpf',
            field=models.CharField(max_length=14, validators=[FormApp.validators.validateCPF], verbose_name='CPF'),
        ),
    ]
