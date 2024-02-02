vazio = " "
simbolo = ["X", "O"]

def criarTabuleiro():
    tabuleiro = [
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
        [vazio, vazio, vazio],
    ]
    return tabuleiro

def imprimirTabuleiro(tabuleiro):
    for i in range(3):
        print("|".join(tabuleiro[i]))
        if(i < 2):
            print("------")

def obterImputValido(mensagem):
    try:
        n = int(input(mensagem))
        if 1 <= n <= 3:
            return n - 1
        else:
            print("Número precisa estar entre 1 e 3")
            return obterImputValido(mensagem)
    except ValueError:
        print("Número não válido")
        return obterImputValido(mensagem)

def verificarMovimento(tabuleiro, i, j):
    if(tabuleiro[i][j] == vazio):
        return True
    return False

def realizarMovimento(tabuleiro, i, j, jogador):
    tabuleiro[i][j] = simbolo[jogador]

def verificarGanhador(tabuleiro):
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
    if (tabuleiro[0][2] == tabuleiro[1][1] and tabuleiro[1][1] == tabuleiro[2][0] and tabuleiro[0][2] != vazio):
            return tabuleiro[0][2]

    for i in range(3):
        for j in range(3):
            if(tabuleiro[i][j] == vazio):
                return False

    return "EMPATE"