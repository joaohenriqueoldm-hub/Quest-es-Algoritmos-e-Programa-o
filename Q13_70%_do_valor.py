# Entrada - inserir o valor em reais
valor_original = float(input("Digite o valor em reais:"))

# Calculando 70% do valor original
porcentagem = ((valor_original / 10) * 3)
novo_valor = valor_original - porcentagem

# Exibindo o resultado
print(f"O novo valor é: R${novo_valor}")