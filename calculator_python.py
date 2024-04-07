def calculator(consumption: list, distributor_tax: float, tax_type: str) -> tuple:
    
    consumo_medio =   calcular_consumo_medio(consumption,distributor_tax)
    desconto = calcular_desconto(consumo_medio,tax_type)
    cobertura = calcular_cobertura(consumo_medio)
    
    economia_mensal = consumo_medio  * desconto * cobertura
    economia_anual = economia_mensal * 12
   
    return (
        round(economia_anual, 2),
        round(economia_mensal, 2),
        round(desconto, 2),
        round(cobertura, 2),
    )


    # Os outros testes foram ajustados de acordo com as correções feitas no código

def calcular_desconto(consumo_medio:float , tax_type:float):
    desconto_total ={
        "Industrial":[0.18,0.15, 0.12],
        "Comercial":[ 0.22,0.18,0.16],
        "Residencial":[0.25,0.22,0.18]
    }
    desconto = 0
    
    if consumo_medio > 20000:
        desconto = desconto_total[tax_type][0]
    elif 10000 <= consumo_medio <= 20000:
        desconto = desconto_total[tax_type][1]            
    else:
        desconto = desconto_total[tax_type][2]  
    return  desconto

def calcular_cobertura(consumo_medio:float):
    cobertura = 0

    if consumo_medio > 20000:
        cobertura = 0.99
    elif 10000 <= consumo_medio <= 20000:
        cobertura = 0.95
    else:
        cobertura = 0.90   
    return cobertura         

def calcular_consumo_medio(consumption:list , distributor_tax:float):
    consumo_medio= sum(consumption)/len(consumption)
    return consumo_medio * distributor_tax

if __name__ == "__main__":
    print("Testing...")

    assert calculator([1518, 1071, 968], 0.95871974, "Industrial") == (
        1473.19,
        122.77,
        0.12,
        0.9,
    )

    assert calculator([1000, 1054, 1100], 1.12307169, "Residencial") == (
        2295.32,
        191.28,
        0.18,
        0.9,
    )

    assert calculator([973, 629, 726], 1.04820025, "Comercial") == (
        1405.56,
        117.13,
        0.16,
        0.9,
    )

    assert calculator([15000, 14000, 16000], 0.95871974, "Industrial") == (
        24591.16,
        2049.26,
        0.15,
        0.95,
    )

    assert calculator([12000, 11000, 11400], 1.12307169, "Residencial") == (
        32297.74,
        2691.48,
        0.22,
        0.95,
    )

    assert calculator([17500, 16000, 16400], 1.04820025, "Comercial") == (
        35776.75,
        2981.40,
        0.18,
        0.95,
    )

    assert calculator([30000, 29000, 29500], 0.95871974, "Industrial") == (
        60478.73,
        5039.89,
        0.18,
        0.99,
    )

    assert calculator([22000, 21000, 21400], 1.12307169, "Residencial") == (
        71602.56,
        5966.88,
        0.25,
        0.99,
    )

    assert calculator([25500, 23000, 21400], 1.04820025, "Comercial") == (
        63832.12,
        5319.34,
        0.22,
        0.99,
    )

    print("Everything passed")