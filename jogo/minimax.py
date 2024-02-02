from jogo_da_velha import vazio, simbolo

def movimentoIA(board, jogador):
    possibilidades = getPosicoes(board)
    melhor_valor = None
    melhor_movimento = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = simbolo[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = vazio
        if(melhor_valor is None):
            melhor_valor = valor
            melhor_movimento = possibilidade
        elif(jogador == 0):
            if(valor > melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade
        elif(jogador == 1):
            if(valor < melhor_valor):
                melhor_valor = valor
                melhor_movimento = possibilidade

    return melhor_movimento[0], melhor_movimento[1]

def getPosicoes(board):
    posicoes = []
    for i in range(3):
        for j in range(3):
            if(board[i][j] == vazio):
                posicoes.append([i, j])
    
    return posicoes

score = {
    "EMPATE": 0,
    "X": 1,
    "O": -1,
    " ": 0  
}

def minimax(board, jogador):
    # Expansão da árvore
    possibilidades = getPosicoes(board)
    
    melhor_valor = None
    for possibilidade in possibilidades:
        board[possibilidade[0]][possibilidade[1]] = simbolo[jogador]
        valor = minimax(board, jogador)
        board[possibilidade[0]][possibilidade[1]] = vazio

        # Backtracking: atualiza o melhor valor com base no valor do nó atual
        if melhor_valor is None:
            melhor_valor = valor
        elif jogador == 0:
            if valor > melhor_valor:
                melhor_valor = valor
        elif jogador == 1:
            if valor < melhor_valor:
                melhor_valor = valor

    return melhor_valor