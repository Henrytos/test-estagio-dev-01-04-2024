from django.db import models


class ConsumptionRules(models.Model):
    CONSUMER_TYPES = (
        ('residencial', 'Residencial'),
        ('comercial', 'Comercial'),
        ('industrial', 'Industrial'),
    )
    
    consumer_type = models.CharField("Tipo de Consumidor", max_length=20, choices=CONSUMER_TYPES)
    
    consumption = models.FloatField("consumo",)
    cover = models.FloatField("cobertura",)
    discount = models.IntegerField("valor_com_desconto",)
    def __str__(self):
        return f"{self.consumer_type} - R${self.consumption} - R${self.discount}"

class Consumer(models.Model):
    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField(
        "Tarifa da Distribuidora", blank=True, null=True
    )
    #  create the foreign key for discount rule model here
    consumption_rule = models.ForeignKey(ConsumptionRules, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Regra de Desconto")

    def __str__(self):
        return f"{self.name} - {self.city} - {self.state}"

# TODO: Create the model DiscountRules below
"""Fields:
-> Consumer type  
-> Consumption range
-> Cover value
-> Discount value
The first three fields should be a select with the values provided in the table
defined in the readme of the repository. Discount should be numerical
"""

# TODO: You must populate the consumer table with the data provided in the file consumers.xlsx
#  and associate each one with the correct discount rule



