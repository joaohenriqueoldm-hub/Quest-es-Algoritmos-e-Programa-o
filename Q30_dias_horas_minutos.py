# Entrada - inserir o valor em minutos
valor_em_minutos = int(input("Digite o valor em minutos:"))

# Processamento - dias, horas e minutos
dias = valor_em_minutos // 1440
horas = (valor_em_minutos % 1440) // 60
minutos = (valor_em_minutos % 1440) % 60

# Exibir resultado
print(f"{valor_em_minutos} horas são iguais a {dias} dias, {horas} horas e {minutos} minutos.")