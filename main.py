def visualizar_tabuleiro(tabuleiro):
    cont = 0
    for linha in tabuleiro:
        print(f"{linha[0]} | {linha[1]} | {linha[2]}")
        if(cont < 2):
            print('-' * 10)
            cont += 1
    print()



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


def verificar_empate(tabuleiro):
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
     
    while True:
        visualizar_tabuleiro(tabuleiro)
        print(f"É a vez do {jogador}")
        
        try:
            linha = int(input("Informe a posição da linha [de 0 a 2]: "))
            coluna = int(input("Informe a posição da coluna [de 0 a 2]: "))
            
            if(linha < 0 or linha > 2) or (coluna < 0 or coluna > 2) or (tabuleiro[linha][coluna] != " "):
                print("\033[31mJogada inválida! Tente novamente.\033[0m\n")
                continue
            
            tabuleiro[linha][coluna] = jogador
            
            if verificar_vencedor(tabuleiro, jogador):
                visualizar_tabuleiro(tabuleiro) 
                print(f"\033[32mO jogador {jogador} venceu!\033[0m")
                break
            
            if verificar_empate(tabuleiro):
                visualizar_tabuleiro(tabuleiro)
                print("\033[33mEMPATE\033[0m")
                break
            
            # Operador ternário
            jogador = "O" if jogador == "X" else "X"
        
        except ValueError:
            print("\033[31mEntrada inválida. Por favor, insira um número inteiro de 0 e 2.\033[0m\n")
        
        
jogar()