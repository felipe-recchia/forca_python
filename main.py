from funcoes import *

def iniciar_jogo():
    # Definir o nivel de dificuldade
    categoria = (input("\nEscolha o nível de dificuldade \n\nFácil   [1] \nMédio   [2] \nDifícil [3]:\n\n"))

    # Definir quantidade de jogadores
    numero_jogadores = int(input("Digite a quantidade de jogadores: "))

    # Definir quantidade de rodadas
    numero_rodadas = int(input("Digite a quantidade de rodadas: "))

    resultados_jogadores = []

    # Loop para jogar com cada jogador
    for jogador_num in range(1, numero_jogadores + 1):
        jogador = []
        print(f"\nJogador {jogador_num}:")
        saldo_final=0

        for rodada in range(1, numero_rodadas + 1):
            print(f"Rodada {rodada}:")

            # Selecionar categoria e palavra
            palavra = sortear_palavra(categoria)

            # Jogar a rodada
            vidas = 6
            jogar_rodada(palavra, vidas)

        print("- " * 20)

        # Adiciona o número do jogador à lista de resultados
        jogador.append(jogador_num)

        # Verifica se o jogador já existe na lista de resultados
        jogador_existe = False
        for i, (jogador_antigo, saldo_antigo) in enumerate(resultados_jogadores):
            if jogador_antigo == jogador:
                # Atualiza o saldo final do jogador
                resultados_jogadores[i] = (jogador, saldo_antigo + saldo_final)
                jogador_existe = True
                break

        # Se o jogador não existir na lista, adiciona-o
        if not jogador_existe:
            resultados_jogadores.append((jogador, saldo_final))

    # Classificar os resultados por saldo final
    resultados_jogadores.sort(key=lambda x: x[1], reverse=True)

    # Imprimir o ranking dos jogadores
    print("\nRanking dos Jogadores:")
    if resultados_jogadores:
        for i, resultado in enumerate(resultados_jogadores, start=1):
            if isinstance(resultado, tuple) and len(resultado) == 2 and isinstance(resultado[0], list) and isinstance(resultado[1], (int, float)):
                jogador, saldo_final = resultado
                print(f"{i}. Jogador {jogador[0]}: Saldo Final = {saldo_final}")
            else:
                print(f"Erro: Resultado inválido na posição {i}: {resultado}")
    else:
        print("Nenhum jogador no ranking.")

# Executa o jogo
if __name__ == "__main__":
    iniciar_jogo()