# Entrada - inserir o valor em segundos
valor_em_segundos = int(input("Digite o valor em segundos:"))

# Processamento - horas, segundos e minutos
horas = valor_em_segundos // 3600
minutos = ((valor_em_segundos % 3600) // 60)
segundos = ((valor_em_segundos % 3600) % 60)

# Exibir resultado
print(f"{valor_em_segundos} segundos são iguais a {horas} horas, {minutos} minutos e {segundos} segundos.")
