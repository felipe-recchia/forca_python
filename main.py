from funcoes import *

# Executa o jogo
def iniciar_jogo():
    
    # Verificar se há um estado de jogo salvo
    estado_jogo = carregar_estado_jogo()

    if estado_jogo:
        # Se houver um arquivo de jogo salvo, pergunta ao jogador se ele deseja carregar o jogo
        carregar = input("Há um jogo salvo. Deseja carregar o jogo salvo? (s/n): ")
        if carregar.lower() == 's':
            # Se o jogador escolher carregar o jogo, carrega o estado do jogo salvo
            palavra = estado_jogo['palavra']
            letras_acertadas = estado_jogo['letras_acertadas']
            vidas = estado_jogo['vidas']
            jogador_num = estado_jogo['jogador_num']
            saldo_final = estado_jogo['saldo_final']
            print("Estado do jogo carregado.")
            print(f"Você acertou: {letras_acertadas}")
            print(f"Você tem: {vidas} vidas")
            print(f"Jogador: {jogador_num}")

            return jogar_rodada(palavra, vidas, jogador_num)
        else:
          # Se o jogador não deseja carregar um jogo, inicia um novo jogo
          iniciar_novo_jogo()
    else:
      # Se não houver um estado de jogo salvo, inicia um novo jogo
      iniciar_novo_jogo()

def iniciar_novo_jogo():
    # Definir o nivel de dificuldade
      categoria = (input("\nEscolha o nível de dificuldade \n\nFácil   [1] \nMédio   [2] \nDifícil [3]:\n\n"))

      # Lista para armazenar os jogadores e seus nomes
      jogadores = []

      # Definir quantidade de jogadores
      numero_jogadores = int(input("Digite a quantidade de jogadores: "))

      # Definir quantidade de rodadas
      numero_rodadas = int(input("Digite a quantidade de rodadas: "))
      palavra, letras_acertadas, vidas, jogador_num = "", [], 6, 0

         # Pedir os nomes dos jogadores
      for jogador_num in range(1, numero_jogadores + 1):
          nome_jogador = input(f"Digite o nome do Jogador {jogador_num}: ")
          jogadores.append(nome_jogador)

          resultados_jogadores = []

      # Loop para jogar com cada jogador
      for jogador_num, nome_jogador in enumerate(jogadores, start=1):
        print(f"\nJogador {jogador_num} ({nome_jogador}):")
        saldo_final_total=0

        for rodada in range(1, numero_rodadas + 1):
            print(f"Rodada {rodada}:")

            # Sortear a palavra
            palavra = sortear_palavra(categoria)
           
            # Jogar a rodada
            vidas = 6
            saldo_final = jogar_rodada(palavra, vidas, jogador_num)
            saldo_final_total += vidas + saldo_final

            # Verificar se o jogador deseja salvar o estado do jogo
            salvar = input("Deseja salvar o estado do jogo? (s/n): ").lower()
            if salvar == "s":
                salvar_estado_jogo(palavra, letras_acertadas, vidas, jogador_num, saldo_final)
                print("Estado do jogo salvo.")

        print("- " * 20)

        # Adiciona o número do jogador à lista de resultados
        resultados_jogadores.append((jogador_num, saldo_final_total))

        # Classificar os resultados por saldo final
        resultados_jogadores.sort(key=lambda x: x[1], reverse=True)

       # Imprimir o ranking dos jogadores
      print("\nRanking dos Jogadores:")
      if resultados_jogadores:
          for i, (jogador, saldo_final) in enumerate(resultados_jogadores, start=1):
           print(f"{i}. Jogador {jogador}: Pontuação Final = {saldo_final}")

# Executa o jogo
if __name__ == "__main__":
    iniciar_jogo()