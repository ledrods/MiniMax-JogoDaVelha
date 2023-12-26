vazio = " "

def criar_tabuleiro():
    tabuleiro = [
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
    ]
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
    for i in range(3):
        print("|".join(tabuleiro[i]))
        if(i < 2):
            print("----------")

def obter_input_valido(mensagem):
    try:
        n = int(input(mensagem))
        if 1 <= n <= 3:
            return n - 1
        else:
            print("Número precisa estar entre 1 e 3")
            return obter_input_valido(mensagem)
    except ValueError:
        print("Número não válido")
        return obter_input_valido(mensagem)

def verificar_movimento():
    pass

def realizar_movimento():
    pass

def verificar_ganhador(tabuleiro):
    pass
