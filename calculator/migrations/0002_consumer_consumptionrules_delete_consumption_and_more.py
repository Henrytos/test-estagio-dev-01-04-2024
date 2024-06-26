# Generated by Django 5.0.3 on 2024-04-06 23:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nome do Consumidor')),
                ('document', models.CharField(max_length=14, unique=True, verbose_name='Documento(CPF/CNPJ)')),
                ('zip_code', models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP')),
                ('city', models.CharField(max_length=128, verbose_name='Cidade')),
                ('state', models.CharField(max_length=128, verbose_name='Estado')),
                ('consumption', models.IntegerField(blank=True, null=True, verbose_name='Consumo(kWh)')),
                ('distributor_tax', models.FloatField(blank=True, null=True, verbose_name='Tarifa da Distribuidora')),
            ],
        ),
        migrations.CreateModel(
            name='ConsumptionRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumption', models.FloatField(verbose_name='consumo')),
                ('cover', models.FloatField(verbose_name='cobertura')),
                ('discount', models.IntegerField(verbose_name='desconto')),
            ],
        ),
        migrations.DeleteModel(
            name='Consumption',
        ),
        migrations.AddField(
            model_name='consumer',
            name='ConsumptionRule',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='calculator.consumptionrules'),
        ),
    ]
