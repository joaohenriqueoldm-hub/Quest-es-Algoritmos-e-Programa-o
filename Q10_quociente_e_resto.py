# Entrada digitar os dois números que serão utilizados
n_1 = int(input("Digite o primeiro número:"))
n_2 = int(input("Digite o segundo número:"))

# Dividir os números e encontrar o quociente e o resto
# Quociente
q = n_1 // n_2 
# Resto
r = n_1 % n_2

# Exibir o resultado
print(f"Realizando a divisão de {n_1} por {n_2} o quociente é {q} e o resto é {r}")