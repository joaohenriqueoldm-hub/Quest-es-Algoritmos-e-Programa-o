# Entrada - inserir o valor em dias
valor_em_dias = int(input("Digite o valor em dias:"))

# Processamento - semanas e dias
semanas = valor_em_dias // 7
dias = valor_em_dias % 7

# Exibir resultado
print(f"{valor_em_dias} dias são iguais a {semanas} semanas e {dias} dias")

