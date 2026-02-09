# Entrada do valor em minutos
min = int(input("Digite o valor em minutos:"))

# Transfromando em horas e minutos
horas = min // 60
minutos = min % 60

# Resultado
print(f"{min} minutos são iguais a {horas} horas e {minutos} minutos")