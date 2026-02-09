# Entrada - inserir quantidade de anos que fuma, quantidade de cigarros diários e preço da carteira de cigarro
anos = int(input("Digite há quantos anos você fuma:"))
cigarros_diarios = int(input("Digite quantos cigarros você fuma por dia:"))
preco = float(input("Digite quanto custa uma carteira de cigarro:"))

# Processamento - calcular o gasto em cigarros
custo_unidade = preco / 20
custo_diario = custo_unidade * cigarros_diarios
custo_anual = custo_diario * 365
gasto_total = custo_anual * anos

# Exibir o resultado
print(f"O gasto total com cigarros é de {gasto_total} reais")

