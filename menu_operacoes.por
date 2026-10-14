programa
{
    funcao inicio()
    {
        inteiro opcao
        real numero1, numero2, resultado

        escreva("===== MENU DE OPERACOES =====\n")
        escreva("1 - Soma\n")
        escreva("2 - Subtracao\n")
        escreva("3 - Multiplicacao\n")
        escreva("4 - Divisao\n")

        escreva("Escolha uma operacao: ")
        leia(opcao)

        escreva("Digite o primeiro numero: ")
        leia(numero1)

        escreva("Digite o segundo numero: ")
        leia(numero2)

        escolha (opcao)
        {
            caso 1:
                resultado = numero1 + numero2
                escreva("Resultado: ", resultado)
                pare

            caso 2:
                resultado = numero1 - numero2
                escreva("Resultado: ", resultado)
                pare

            caso 3:
                resultado = numero1 * numero2
                escreva("Resultado: ", resultado)
                pare

            caso 4:
                se (numero2 != 0)
                {
                    resultado = numero1 / numero2
                    escreva("Resultado: ", resultado)
                }
                senao
                {
                    escreva("Nao e possivel dividir por zero.")
                }
                pare

            caso contrario:
                escreva("Opcao invalida.")
        }
    }
}