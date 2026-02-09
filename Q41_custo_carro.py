# Entrada - inserir o custo de fábrica do carro
custo_fabrica = float(input("Digite o custo de fábrica do carro:"))

# Processamento - calcular o custo para o consumidor com impostos e a parcela do distribuidor
p_impostos = (custo_fabrica / 100) * 28
p_distribuidor = (custo_fabrica / 100) * 45
custo_consumidor = custo_fabrica + p_distribuidor + p_impostos

# Resultado
print(f"O custo para o consumidor após impostos e a parcela do distribuidor é: {custo_consumidor:.2f}")


