# Entrada - inserir numerador e denominador da primeira fração
n1 = int(input("Digite o numerador da primeira fração: "))
d1 = int(input("Digite o denominador da primeira fração: "))

# Entrada - inserir numerador e denominador da segunda fração
n2 = int(input("Digite o numerador da segunda fração: "))
d2 = int(input("Digite o denominador da segunda fração: "))

# Soma das frações
numerador_final = n1 * d2 + n2 * d1
denominador_final = d1 * d2

# Exibir o resultado
print(f"Soma das frações {n1}/{d1} e {n2}/{d2} é igual a {numerador_final}/{denominador_final}")
