def exchange_money(budget, exchange_rate):
    resultado = budget / exchange_rate
    return resultado
print("Resultado en Japón:", exchange_money(300, 0.0075)) 

print("Resultado en México:", exchange_money(500, 0.055))

print("Resultado en Colombia:", exchange_money(100, 0.00025))
