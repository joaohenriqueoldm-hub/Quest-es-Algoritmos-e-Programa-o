# Entrada - Inserir o número binário
binario = input("Digite um número binário de quatro dígitos:")

# Processamento - convertendo de binário para a base decimal
numero_1 = ((binario // 1000)) * 8
numero_2 = ((binario % 1000) // 100) * 4
numero_3 = (((binario % 1000) % 100) // 10) * 2
numero_4 = (((binario % 1000) % 100) % 10) * 1

decimal = numero_1 + numero_2 + numero_3 + numero_4

# Exibir o resultado
print(f"O número binário {binario} é equivalente a {decimal} na base decimal ")


