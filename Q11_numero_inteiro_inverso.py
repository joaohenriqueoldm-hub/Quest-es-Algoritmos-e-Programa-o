# Entrada digitar um número de três dígitos
numero = int(input("Digite um número inteiro de três digitos:"))

# Processamento - invertendo os dígitos
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10
novo_numero = centena + dezena * 10 + unidade * 100

# Exibir o resultado
print(f"Número invertido: {novo_numero}")
