# Entrada digitar um número de três dígitos
numero = int(input("Digite um número inteiro de três digitos:"))

# 1 - Processamento - invertendo os dígitos
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10
novo_numero = centena + dezena * 10 + unidade * 100

# 2 - Processamento - subtraindo o numero original pelo inverso
diferenca = numero - novo_numero

# Exibir o resultado
print(f"{numero} - {novo_numero} é igual a {diferenca}")
