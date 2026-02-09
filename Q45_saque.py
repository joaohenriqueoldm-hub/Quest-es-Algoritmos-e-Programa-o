# Entrada - inserir a quantidade que vai ser sacada
saque = float(input("Digite quanto vai ser sacado:"))

# Calculando quantas notas de cada serão sacadas com base na distribuição ótima
nota_de_100 = saque // 100
nota_de_50 = (saque % 100) // 50
nota_de_20 = ((saque % 100) % 50) // 20
nota_de_10 = (((saque % 100) %50) % 20) // 10
nota_de_5 = (saque % 10) // 5
nota_de_2 = ((saque % 10) % 5) // 2
moeda_de_1 = (((saque % 10) % 5 ) % 2)

# Exibir o resultado
print(f"R${saque} sacados em {nota_de_100} notas de 100, {nota_de_50} de 50, {nota_de_20} de 20, {nota_de_10} de 10, {nota_de_5} de 5, {nota_de_2} de 2, {moeda_de_1} moedas de 1 real")