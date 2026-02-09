# Entrada - digitar os ponto do plano: ponto 1 (x1,y1), ponto 2 (x2,y2)
x1 = float(input("Digite x1: "))
y1 = float(input("Digite y1: "))
x2 = float(input("Digite x2: "))
y2 = float(input("Digite y2: "))

# Calcular a distancia entre os pontos
distancia = ((x1 - x2)**2 + (y1 - y2)**2) ** 0.5

# Resultado
print(f"A distância entre os pontos 1 e 2 é: {distancia:.2f}")

