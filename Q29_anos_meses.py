# Entrada - Inserir valor em meses
mes = int(input("Digite o valor em meses:"))

# Processamento - anos e meses
anos = mes // 12
meses = mes % 12

# Exibir o resultado
print(f"{mes} equivale a {anos} anos e {meses} meses")
