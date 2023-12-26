from jogo_da_velha import criar_tabuleiro, realizar_movimento, obter_input_valido, \
                            imprimir_tabuleiro, verificar_ganhador, verificar_movimento

jogador = 0 
tabuleiro = criar_tabuleiro()
ganhador = verificar_ganhador(tabuleiro)
while not ganhador:
    imprimir_tabuleiro(tabuleiro)
    i = obter_input_valido("Digite a linha")
    j = obter_input_valido("Digite a coluna")
    
    if(verificar_movimento(tabuleiro, i, j)):
        realizar_movimento()
