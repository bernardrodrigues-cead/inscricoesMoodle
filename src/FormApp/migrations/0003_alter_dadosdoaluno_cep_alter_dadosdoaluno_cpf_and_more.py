# Generated by Django 4.1.1 on 2022-09-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormApp', '0002_remove_dadosdoaluno_rua_dadosdoaluno_logradouro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dadosdoaluno',
            name='cep',
            field=models.CharField(max_length=9, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='dadosdoaluno',
            name='cpf',
            field=models.CharField(max_length=14, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='dadosdoaluno',
            name='siape',
            field=models.CharField(blank=True, max_length=7, null=True, verbose_name='SIAPE'),
        ),
        migrations.AlterField(
            model_name='dadosdoaluno',
            name='telefone',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='dadosdoaluno',
            name='uf',
            field=models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF'),
        ),
    ]