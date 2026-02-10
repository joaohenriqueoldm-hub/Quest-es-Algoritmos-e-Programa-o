# Entrada digitar os dois números que serão utilizados
numero_1 = float(input("Digite o primeiro número:"))
numero_2 = float(input("Agora o segundo número:"))

# Calculando a soma dos dois números
soma = numero_1 + numero_2

# Calculando a diferença entre os dois números
diferenca = numero_1 - numero_2

# Calculando a divisão entre a soma e a diferença dos dois números
divisao = soma / diferenca

# Resultado
print(f"O resultado da divisão entre {soma} e {diferenca} é: {divisao:.2f}")
