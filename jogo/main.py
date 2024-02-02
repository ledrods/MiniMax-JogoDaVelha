from jogo_da_velha import criarTabuleiro, realizarMovimento, imprimirTabuleiro, verificarGanhador, verificarMovimento
from minimax import movimentoIA

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

jogador = 0 # jogador 0
board = criarTabuleiro()
ganhador = verificarGanhador(board)

while not ganhador:
    imprimirTabuleiro(board)
    print("===================")
    
    if jogador == 0:
        i, j = movimentoIA(board, jogador)
    else:
        print(f"Jogador humano ({'X' if jogador == 0 else 'O'}), é sua vez.")
        i = obterImputValido("Digite a linha (1, 2 ou 3): ")
        j = obterImputValido("Digite a coluna (1, 2 ou 3): ")

    if verificarMovimento(board, i, j):
        realizarMovimento(board, i, j, jogador)
        jogador = (jogador + 1) % 2
    else:
        print("A posição informada já está ocupada")

    ganhador = verificarGanhador(board)

print("===================")
imprimirTabuleiro(board)
print("Ganhador =", ganhador)
print("===================")