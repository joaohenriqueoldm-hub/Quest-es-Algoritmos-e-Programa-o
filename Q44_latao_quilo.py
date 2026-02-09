# Entrada - digitar a quantidade de latão em quilogramas
latao = float(input("Digite a quantidade de latão em kg:"))

# Processamento - calcular a quantidade que será necessária de cobre e zinco
cobre = (latao / 100) * 70
zinco = (latao / 100) * 30

# Exibir o resultado
print(f"Para se obter {latao} kg de latão serão necessários {cobre} kg de cobre e {zinco} kg de zinco")