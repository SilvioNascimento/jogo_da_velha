def visualizar_tabuleiro(tab):
    tabuleiro = tab
    cont = 0
    for linha in tabuleiro:
        print(f"{linha[0]} | {linha[1]} | {linha[2]}")
        if(cont < 2):
            print('-' * 10)
            cont += 1
    print()
        

def add_peca_no_tabuleiro(tab, linha, coluna, jogador):
    tabuleiro = tab
    try:
        if(tabuleiro[linha][coluna] == " "):
            tabuleiro[linha][coluna] = jogador
            visualizar_tabuleiro(tabuleiro)
            
        else:   # Colocar esta parte na parte final do jogo
            print("\033[31mErro: a posição informada já está ocupada\033[0m")
        
    except IndexError:
        print("\033[31mErro: a posição informada está fora de alcance do tabuleiro\033[0m")


def verificar_vencedor(tabuleiro, jogador):
    # Verificando as linhas
    for linha in tabuleiro:
        if linha[0] == linha[1] == linha[2] == jogador:
            return True
    
    # Verificando as colunas
    for i in range(3):
        if tabuleiro[0][i] == tabuleiro[1][i] == tabuleiro[2][i] == jogador:
            return True
    
    # Verificando as diagonais
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] == jogador:
        return True
    
    return False


def verificar_empate(tab):
    tabuleiro = tab
    for linha in tabuleiro:
        for casa in linha:
            if casa == " ":
                return False
    return True
        

def jogar():
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]
    jogador = "X"
    
    visualizar_tabuleiro(tabuleiro)
    
    while True:
        print(f"É a vez do {jogador}")
        linha = int(input("Informe a posição da linha [de 0 a 2]: "))
        coluna = int(input("Informe a posição da coluna [de 0 a 2]: "))
        
        if(linha < 0 or linha > 2) or (coluna < 0 or coluna > 2) or (tabuleiro[linha][coluna] != " "):
            print("Jogada inválida! Tente novamente.")
            continue
        
        add_peca_no_tabuleiro(tabuleiro, linha, coluna, jogador)
        
        if verificar_vencedor(tabuleiro, jogador):
            print(f"O jogador {jogador} venceu!")
            break
        
        if verificar_empate(tabuleiro):
            print("EMPATE")
            break
        
        jogador = "O" if jogador == "X" else "X"
        
        
jogar()