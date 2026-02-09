# Entrada - inserir o valor em horas
valor_em_horas = int(input("Digite o valor em horas:"))

# Processamento - semanas, dias e horas
semanas = valor_em_horas // 168
dias = (valor_em_horas % 168) // 24
horas = valor_em_horas % 24

# Exibir resultado
print(f"{valor_em_horas} horas são iguais a {semanas} semanas, {dias} dias e {horas} horas.")