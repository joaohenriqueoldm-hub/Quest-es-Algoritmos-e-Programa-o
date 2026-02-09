# Entrada - inserir o valor da mercadoria
valor = int(input("Digite o valor da mercadoria: "))

# Calculando o valor das prestações e da entrada
prestacao = valor // 3
entrada = valor - 2 * prestacao

print(f"A mercadoria de valor: R${valor} ficará com uma entrada de R${entrada} e duas parcelas iguais de R${prestacao}")

