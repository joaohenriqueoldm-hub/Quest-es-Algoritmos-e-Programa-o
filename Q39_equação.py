# Entrada - inserir três números inteiros e positivos
a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))

# 1 - Processamento - calcular R e S
r = (a + b) ** 2
s = (b + c) ** 2

# 2 - Processamento - resolver a equação
d = (r + s) / 2

# Exibir o resultado
print(f"O resultado da equaçao é: D = {d}")
