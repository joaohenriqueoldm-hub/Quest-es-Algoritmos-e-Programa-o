# Entrada - inserir os coeficientes a, b, c, d, e, f
a = float(input("Digite o coeficiente a:"))
b = float(input("Digite o coeficiente b:"))
c = float(input("Digite o coeficiente c:"))
d = float(input("Digite o coeficiente d:"))
e = float(input("Digite o coeficiente e:"))
f = float(input("Digite o coeficiente f:"))

# Processamento - calcular x e y
x = ((c * e) - (b * f)) / ((a * e) - (b * d))
y = ((a * f) - (c * d)) / ((a * e) - (b * d))

# Exibir o resultado
print(f"O resultado é: x = {x} e y = {y}")