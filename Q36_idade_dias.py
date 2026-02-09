# Entrada - inserir a idade em anos, meses e dias
anos = int(input("Digite quantos anos de idade você tem:"))
meses = int(input("E quantos meses de idade você tem:"))
dias = int(input("E quantos dias de idade você tem:"))

# Processamento - transformar anos, meses e dias em dias
idade = (anos * 365) + (meses * 30) + dias

# Exibir o resultado
print(f"{anos} anos,{meses} meses e {dias} dias é equivalente a {idade} dias de idade")