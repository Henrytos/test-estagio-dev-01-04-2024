from django.shortcuts import render
from .models import Consumer ,ConsumptionRules
from calculator_python import calculator

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

def home(request):
    if request.method=="POST":
        rate_one =  int(request.POST["rate_one"])
        rate_two =  int(request.POST["rate_two"])
        rate_three =  int(request.POST["rate_three"])
        distributor_tax = float(request.POST['rate_value'])
        tax_type = request.POST['rate_type']
        
        calculator([rate_one,rate_two,rate_three],distributor_tax,tax_type)
        # calculadora = Consumption(
        #     consumo_mes1=rate_one,
        #     consumo_mes2=rate_two,
        #     consumo_mes3=rate_three,
        #     tarifa_distribuidora=rate_value,
        #     tipo_tarifa=rate_type
        # )
        # calculadora.save()
        return render(request,'home.html')
    else:
        return render(request,'home.html')