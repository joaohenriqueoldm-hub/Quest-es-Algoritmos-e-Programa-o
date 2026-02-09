# Entrada do número inteiro de 3 digitos
numero = int(input("Digite um numero inteiro de 3 dígitos:"))

# Calculando a soma dos elementos
centena = numero // 100
resto = numero % 100
dezena = resto // 10
unidade = resto % 10 
soma_dos_elementos = centena + dezena + unidade

# Resultado 
print(f"A soma dos dígitos {centena}, {dezena} e {unidade} do número {numero} é igual a {soma_dos_elementos}")
