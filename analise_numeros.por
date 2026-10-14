programa
{
    funcao inicio()
    {
        real numero
        real soma = 0
        real media
        real maior
        real menor

        para (inteiro i = 0; i < 5; i++)
        {
            escreva("Digite o ", i + 1, "º numero: ")
            leia(numero)

            soma = soma + numero

            se (i == 0)
            {
                maior = numero
                menor = numero
            }
            senao
            {
                se (numero > maior)
                {
                    maior = numero
                }

                se (numero < menor)
                {
                    menor = numero
                }
            }
        }

        media = soma / 5

        escreva("\n===== RESULTADO =====\n")
        escreva("Soma: ", soma, "\n")
        escreva("Media: ", media, "\n")
        escreva("Maior valor: ", maior, "\n")
        escreva("Menor valor: ", menor, "\n")
    }
}