from django.db import models



class Consumption(models.Model):
    consumo_mes1 = models.FloatField()
    consumo_mes2 = models.FloatField()
    consumo_mes3 = models.FloatField()
    tarifa_distribuidora = models.FloatField()
    tipo_tarifa_choices = (
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
        ('industrial', 'Industrial'),
    )
    tipo_tarifa = models.CharField(max_length=20, choices=tipo_tarifa_choices)

    # Resultados
    economia_anual = models.FloatField(null=True, blank=True)
    economia_mensal = models.FloatField(null=True, blank=True)
    desconto_aplicado = models.FloatField(null=True, blank=True)
    cobertura = models.FloatField(null=True, blank=True)

    pass