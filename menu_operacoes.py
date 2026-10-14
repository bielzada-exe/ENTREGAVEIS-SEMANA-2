print("===== MENU DE OPERAÇÕES =====") #O que será selecionado no menu de operações
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma operação: "))#o que será selecionado no menu de operações, será armazenado na variável "opcao"

numero1 = float(input("Digite o primeiro número: "))#float, usado para armazenar o primeiro número
numero2 = float(input("Digite o segundo número: "))#float, usado para armazenar o segundo número

match opcao: #estrutura de controle para selecionar a operação

    case 1: #caso a opção 1 seja selecionada
        resultado = numero1 + numero2
        print(f"Resultado: {resultado}")

    case 2: #caso a opção 2 seja selecionada
        resultado = numero1 - numero2
        print(f"Resultado: {resultado}")

    case 3: #caso a opção 3 seja selecionada
        resultado = numero1 * numero2
        print(f"Resultado: {resultado}")

    case 4: #caso a opção 4 seja selecionada
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"Resultado: {resultado}")
        else:
            print("Não é possível dividir por zero.")

    case _:
        print("Opção inválida.")