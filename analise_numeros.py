soma = 0 #variável para armazenar a soma dos números digitados

maior = None 
menor = None

for i in range(5):#loop para ler 5 números

    numero = float(input(f"Digite o {i + 1}º número: "))#float, usado para armazenar o número digitado pelo usuário

    soma += numero #adiciona o número digitado à soma

    if maior is None or numero > maior:
        maior = numero

    if menor is None or numero < menor:
        menor = numero


media = soma / 5

print()
print("===== RESULTADO =====")
print(f"Soma: {soma:.2f}")
print(f"Média: {media:.2f}")
print(f"Maior valor: {maior:.2f}")
print(f"Menor valor: {menor:.2f}")