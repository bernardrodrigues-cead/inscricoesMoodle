# Generated by Django 4.1.1 on 2022-10-10 16:24

import FormApp.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('nome_breve', models.CharField(max_length=31, verbose_name='Nome Breve')),
                ('categoria', models.CharField(choices=[('SIGA/UAB', 'Correspondência no SIGA/UAB'), ('SIGA/Flex', 'Correspondência no SIGA/Flexibilização Curricular'), ('Livre', 'Sem Correspondência no SIGA/Curso Livre')], max_length=9)),
                ('data_inicio', models.DateField(verbose_name='Início das Atividades')),
                ('data_fim', models.DateField(verbose_name='Fim das Atividades')),
                ('matricula_inicio', models.DateTimeField(verbose_name='Início das Inscrições')),
                ('matricula_fim', models.DateTimeField(verbose_name='Fim das Inscrições')),
                ('anexar_documentacao', models.BooleanField(blank=True, default=False, null=True, verbose_name='Anexar Documentação')),
            ],
        ),
        migrations.CreateModel(
            name='DadosDoAluno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('documentacao', models.FileField(blank=True, null=True, upload_to='uploads', validators=[FormApp.validators.validatePDF], verbose_name='Documentação')),
                ('cpf', models.CharField(max_length=14, unique=True, validators=[FormApp.validators.validateCPF], verbose_name='CPF')),
                ('data_nascimento', models.DateField(validators=[FormApp.validators.validateBirthdate], verbose_name='Data de Nascimento')),
                ('nome', models.CharField(help_text='Em caso de nome social, é necessário que o mesmo conste em documento emitido pela \n            Receita Federal ou Instituto de Identificação para emissão do certificado de conclusão/participação com nome social.\n            Em caso de dúvidas, procure os canais de atendimento da Receita Federal. \n        ', max_length=63, verbose_name='Nome/Nome Social')),
                ('sobrenome', models.CharField(max_length=127)),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('cidade', models.CharField(max_length=63)),
                ('telefone', models.CharField(max_length=15)),
                ('cep', models.CharField(max_length=9, verbose_name='CEP')),
                ('logradouro', models.CharField(max_length=255, verbose_name='Logradouro')),
                ('numero', models.IntegerField(verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=255, null=True)),
                ('bairro', models.CharField(max_length=31)),
                ('uf', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2, verbose_name='UF')),
                ('siga', models.BooleanField(verbose_name='É aluno da UFJF?')),
                ('siape', models.CharField(blank=True, max_length=7, null=True, verbose_name='SIAPE')),
                ('data_cadastro', models.DateTimeField(auto_now_add=True)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='FormApp.curso', verbose_name='Curso Pretendido')),
            ],
        ),
    ]
