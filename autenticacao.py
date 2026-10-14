senha_correta = "1234" #senha correta para acesso ao sistema

tentativas = 0 #variável para contar o número de tentativas de login
acesso_liberado = False #variável para indicar se o acesso foi liberado ou não

while tentativas < 3:#loop para permitir até 3 tentativas de login

    senha = input("Digite sua senha: ")#string, usado para armazenar a senha digitada pelo usuário

    tentativas += 1

    if senha == senha_correta:

        print("Acesso liberado!")
        acesso_liberado = True
        break

    else:#caso a senha digitada seja incorreta

        print("Senha incorreta.")

        tentativas_restantes = 3 - tentativas

        if tentativas_restantes > 0:
            print(f"Tentativas restantes: {tentativas_restantes}")

if not acesso_liberado:#caso o acesso não tenha sido liberado após 3 tentativas
    print("Acesso bloqueado. Você excedeu o limite de tentativas.")