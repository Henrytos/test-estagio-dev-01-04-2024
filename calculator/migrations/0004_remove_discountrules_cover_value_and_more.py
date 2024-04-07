# Generated by Django 5.0.3 on 2024-04-07 01:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_discountrules_delete_consumption'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discountrules',
            name='cover_value',
        ),
        migrations.RemoveField(
            model_name='discountrules',
            name='discount_value',
        ),
        migrations.AddField(
            model_name='consumer',
            name='consumption_rule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='calculator.discountrules', verbose_name='Regra de Desconto'),
        ),
        migrations.AddField(
            model_name='discountrules',
            name='cover',
            field=models.FloatField(default=1, verbose_name='cobertura'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='discountrules',
            name='discount',
            field=models.IntegerField(default=1, verbose_name='valor_com_desconto'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='discountrules',
            name='consumer_type',
            field=models.CharField(choices=[('residencial', 'Residencial'), ('comercial', 'Comercial'), ('industrial', 'Industrial')], max_length=20, verbose_name='Tipo de Consumidor'),
        ),
        migrations.AlterField(
            model_name='discountrules',
            name='consumption_range',
            field=models.FloatField(verbose_name='consumo'),
        ),
    ]