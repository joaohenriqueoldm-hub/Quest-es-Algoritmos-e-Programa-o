# Entrada do número inteiro de 4 digitos
numero = int(input("Digite um numero inteiro de 4 dígitos:"))

# Calculando a soma dos elementos
milhar = numero // 1000
centena = (numero % 1000) // 100
dezena = (numero % 100) // 10
unidade = ((numero % 100) % 10)
soma_dos_elementos = milhar + centena + dezena + unidade

# Resultado 
print(f"A soma dos dígitos {milhar}, {centena}, {dezena} e {unidade} do número {numero} é igual a {soma_dos_elementos}")
