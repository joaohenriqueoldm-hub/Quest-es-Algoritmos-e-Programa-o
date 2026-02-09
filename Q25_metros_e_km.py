# Entrada - inserir o valor em metros
valor_em_metros = int(input("Digite o valor em metros:"))

# Processamento - quilômetros e metros
km = valor_em_metros // 1000
metros = valor_em_metros % 1000

# Exibir resultado
print(f"{valor_em_metros} m é igual a {km} km e {metros} m")

