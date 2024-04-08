from django.shortcuts import render ,redirect
from calculator_python import calculator
import pandas as pd
from .models import Consumer

# TODO: Your list view should do the following tasks
"""
-> Recover all consumers from the database
-> Get the discount value for each consumer
-> Calculate the economy
-> Send the data to the template that will be rendered
"""


def view1(request):
    # Create the first view here.
    pass


# TODO: Your create view should do the following tasks
"""Create a view to perform inclusion of consumers. The view should do:
-> Receive a POST request with the data to register
-> If the data is valid (validate document), create and save a new Consumer object associated with the right discount rule object
-> Redirect to the template that list all consumers

Your view must be associated with an url and a template different from the first one. A link to
this page must be provided in the main page.
"""


def view2():
    # Create the second view here.
    pass

def populate(request):
    tabela = pd.read_excel("./consumers.xlsx")
    for i , value in tabela.iterrows():
        Consumer.objects.create({
            'name':value['Nome'],
            'document':value['Documento'],
            'zip_code':'',
            'city':value['Cidade'],
            'state':value['Estado'],
            'consumption':float(value['Consumo(kWh)']),
            'distributor_tax':float(value['Tarifa da Distribuidora']),
        })
        
    
    return render(request,render)
    
def list_consumers(request):
    consumers = Consumer.objects.all()
    data = []
    for consumer in consumers:
        economia_anual,economia_mensal,desconto_aplicado,cobertura = calculator([consumer.consumption],consumer.distributor_tax,'A')
        data.append({
            'name':consumer.name,
            'document':consumer.document,
            'economia_anual':economia_anual,
            'economia_mensal':economia_mensal,
            'desconto_aplicado':desconto_aplicado,
            'cobertura':cobertura
        })
    return render(request,'consumers.html',{"data":data})


def home(request):
    if request.method=="POST":
        rate_one =  int(request.POST["rate_one"])
        rate_two =  int(request.POST["rate_two"])
        
        rate_three =  int(request.POST["rate_three"])
        distributor_tax = float(request.POST['distributor_tax'])
        tax_type = request.POST['tax_type']
  
        (economia_anual,
        economia_mensal,
        desconto_aplicado,
        cobertura)=calculator([rate_one,rate_two,rate_three],distributor_tax,tax_type)
        
        # salvar no banco
        # calculadora = Consumption(
        #     consumo_mes1=rate_one,
        #     consumo_mes2=rate_two,
        #     consumo_mes3=rate_three,
        #     tarifa_distribuidora=rate_value,
        #     tipo_tarifa=rate_type
        # )
        # calculadora.save()
        
        desconto = int(desconto_aplicado*100)
        cobertura = int(cobertura*100)
        data={
            "economia_anual":economia_anual,
            "economia_mensal":economia_mensal,
            "desconto":desconto,
            "cobertura":cobertura
        }
        return render(request,'home.html',{"data":data})
    else:
        return render(request,'home.html')