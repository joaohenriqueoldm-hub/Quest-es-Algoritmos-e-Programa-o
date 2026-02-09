# Entrada inserir o valor em graus farenheit
farenheit = float(input("Digite o valor em graus farenheit:"))

# Transformar de farenheit para celsius
celsius = (5 * farenheit - 160) / 9

# Exibir o resultado
print(f"{farenheit} °F são iguais a {celsius} °C")