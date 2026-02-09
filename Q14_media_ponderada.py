# Entrada - Inserir as três notas
nota_1 = float(input("Insira a primeira nota:"))
nota_2 = float(input("Segunda nota:"))
nota_3 = float(input("Terceira nota:"))

# Entrada - Inserir os pesos
peso_1 = float(input("Insira o peso da primeira nota:"))
peso_2 = float(input("Peso da segunda nota:"))
peso_3 = float(input("Peso da terceira nota:"))

# Calcular a média ponderada
soma_das_notas = (nota_1 * peso_1) + (nota_2 * peso_2) + (nota_3 * peso_3)
soma_dos_pesos = peso_1 + peso_2 + peso_3
media_ponderada = soma_das_notas / soma_dos_pesos

# Exibir o resultado
print(f"A média ponderada é igual: {media_ponderada}")