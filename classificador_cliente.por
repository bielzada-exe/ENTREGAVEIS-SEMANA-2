programa
{
    funcao inicio()
    {
        inteiro idade
        real renda

        escreva("Digite a idade do cliente: ")
        leia(idade)

        escreva("Digite a renda mensal do cliente: R$ ")
        leia(renda)

        se (idade >= 30 e renda >= 10000)
        {
            escreva("Categoria do cliente: Diamante")
        }
        senao se (idade >= 25 e renda >= 5000)
        {
            escreva("Categoria do cliente: Ouro")
        }
        senao se (idade >= 18 e renda >= 2500)
        {
            escreva("Categoria do cliente: Prata")
        }
        senao
        {
            escreva("Categoria do cliente: Bronze")
        }
    }
}