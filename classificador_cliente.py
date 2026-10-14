idade = int(input("Digite a idade do cliente: ")) #inteiro, usado para armazenar a idade do cliente
renda = float(input("Digite a renda mensal do cliente: R$ "))#float, usado para armazenar a renda mensal do cliente 

if idade >= 30 and renda >= 10000:
    categoria = "Diamante"
elif idade >= 25 and renda >= 5000:
    categoria = "Ouro"
elif idade >= 18 and renda >= 2500:
    categoria = "Prata"
else: #categoria padrão/se nenhuma das condições anteriores for verdadeira
    categoria = "Bronze"

print(f"Categoria do cliente: {categoria}") #será exibida a categoria do cliente com base na idade e renda informadas