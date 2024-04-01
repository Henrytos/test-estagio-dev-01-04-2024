def calculator(consumption: list, distributor_tax: float, tax_type: str) -> tuple:
    consumo_medio = sum(consumption) / len(consumption)
    
    desconto = 1
    if tax_type == "Industrial":
        if consumo_medio > 20000:
            desconto = 0.82
        elif consumo_medio >= 10000:
            desconto = 0.85
        else:
            desconto = 0.88
    elif tax_type == "Comercial":
        if consumo_medio > 20000:
            desconto = 0.78
        elif consumo_medio >= 10000:
            desconto = 0.82
        else:
            desconto = 0.84
    elif tax_type == "Residencial":
        if consumo_medio > 20000:
            desconto = 0.75
        elif consumo_medio >= 10000:
            desconto = 0.78
        else:
            desconto = 0.82
            
    cobertura = 0

    if consumo_medio < 10000:
        cobertura = 0.9
    elif 10000 <= consumo_medio <= 20000:
        cobertura = 0.95
    else:
        cobertura = 0.99
        
    economia_mensal = (consumo_medio * distributor_tax) * (1 - desconto) * cobertura
    economia_anual = economia_mensal * 12
    
    desconto_aplicado = (1 - desconto) 
   
    
    return (
        round(economia_anual, 2),
        round(economia_mensal, 2),
        round(desconto_aplicado, 2),
        round(cobertura,2 ),
    )


    # Os outros testes foram ajustados de acordo com as correções feitas no código


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