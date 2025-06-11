# libraries
import string as st
import random as rd

# generator functions
def gerar_senha_google():
    letras = st.ascii_letters
    numeros = st.digits
    caracteres = st.punctuation
    conjunto = letras + numeros + caracteres

    senha = ''.join(rd.choice(conjunto) for _ in range(10))
    return senha


def gerar_redes_sociais():
    numeros = st.digits
    caracteres = st.punctuation
    conjunto = numeros + caracteres

    senha = ''.join(rd.choice(conjunto) for _ in range(10))
    return senha


def gerar_senha_WIFI():
    letras = st.ascii_letters
    numeros = st.digits
    caracteres = st.punctuation
    conjunto = letras + numeros + caracteres

    senha = ''.join(rd.choice(conjunto) for _ in range(6))
    return senha


# option menu
def menu():
    print("GERADOR DE SENHAS Trygrid - SUA SEGURANÇA EM PRIMEIRO LUGAR!")
    print("Escolha o tipo de senha para gerar:")
    print("1 - Google")
    print("2 - Redes sociais")
    print("3 - WIFI")
    print("0 - Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == '1':
        senha = gerar_senha_google()
        print("\n[correio de entrega] Sua senha para Google é:", senha)

    elif opcao == '2':
        senha = gerar_redes_sociais()
        print("\n[correio de entrega] Sua senha para redes sociais é:", senha)

    elif opcao == '3':
        senha = gerar_senha_WIFI()
        print("\n[correio de entrega] Sua senha para Wi-Fi é:", senha)

    elif opcao == '0':
        print("\nEncerrando programa. Obrigado por usar o Lionguard a TRygrid Agradece!")
        return

    else:
        print("\n[erro] Opção inválida. Por favor, escolha 1, 2 ou 3.")

    print("\n")
    menu()  # restart the program


# start program
menu()
