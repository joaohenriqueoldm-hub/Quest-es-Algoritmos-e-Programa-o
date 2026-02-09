# Entrada - inserir a idade em dias
idade = int(input("Digite sua idade em dias:"))

# Processamento - transformar dias em anos, meses e dias
anos = idade // 365
meses = (idade % 365) // 30
dias = (idade % 365) % 30

# Exibir o resultado
print(f"{idade} dias é igual a {anos} anos,{meses} meses e {dias} dias de idade")