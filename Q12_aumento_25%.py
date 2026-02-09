# Entrada - Inserir o salário 
salario = float(input("Digite o salário:"))

# Calculando aumento de 25%
novo_salario = salario + (salario / 4) 

# Exibindo o resultado

print(f"Esse é o salário com um aumento de 25%: R${novo_salario:.2f} ")
