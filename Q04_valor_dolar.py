# Entrada do valor do dolar e o valor em dolar que deve ser convertido para real
valor_atual_dolar = float(input("Digite o valor atual do dólar:"))
valor_em_dolar = float(input("Digite o valor em dólar que deve ser convertido:"))

# Transformando o valor em dolar para real
valor_em_reais = valor_em_dolar * valor_atual_dolar

# Resultado
print(f"{valor_em_dolar:.2f} dólares são iguais a R$ {valor_em_reais:.2f}")






