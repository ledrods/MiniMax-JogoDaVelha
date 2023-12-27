vazio = " "
simbolo = ["x", "o"]

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
            print("------")

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

def verificar_movimento(tabuleiro, i, j):
    if(tabuleiro[i][j] == vazio):
        return True
    return False

def realizar_movimento(tabuleiro, i, j, jogador):
    tabuleiro[i][j] = simbolo[jogador]

def verificar_ganhador(tabuleiro):
    #verifica as linhas
    for i in range(3):
        if(tabuleiro[i][0] == tabuleiro[i][1] and tabuleiro[i][1] == tabuleiro[i][2] and tabuleiro[i][0] != vazio):
            return tabuleiro[i][0]
    
    #verifica as colunas
    for i in range(3):
        if(tabuleiro[0][i] == tabuleiro[1][i] and tabuleiro[1][i] == tabuleiro[2][i] and tabuleiro[0][i] != vazio):
            return tabuleiro[0][i]
        
    # diagonal 1
    if (tabuleiro[0][0] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][0] != vazio):
            return tabuleiro[0][0]
    
    # diagonal 2
    if (tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][2] and tabuleiro[0][2] != vazio):
            return tabuleiro[0][0]

    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == vazio):
                return False

    return "Empatou!"