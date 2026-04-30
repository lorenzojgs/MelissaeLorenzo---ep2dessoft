from funcoes import *


def jogo():
    pontuacao = {
        'regra_simples': {1:-1, 2:-1, 3:-1, 4:-1, 5:-1, 6:-1},
        'regra_avancada': {
            'cinco_iguais': -1,
            'full_house': -1,
            'quadra': -1,
            'sem_combinacao': -1,
            'sequencia_alta': -1,
            'sequencia_baixa': -1
        }
    }

    imprime_cartela(pontuacao)

    for _ in range(12):
        guardados = []
        rolados = rolar(guardados)
        contador_rerrolagens = 0
        mostrar_menu = True

        while True:
            if mostrar_menu:
                print("Dados rolados:", rolados)
                print("Dados guardados:", guardados)
                print("Digite 1 para guardar, 2 para remover, 3 para rerrolar, 4 para ver cartela ou 0 para pontuar")

            mostrar_menu = True
            escolha = input()

            if escolha == "1":
                print("Digite o índice do dado a ser guardado (0 a 4):")
                indice = int(input())
                if 0 <= indice < len(rolados):
                    rolados, guardados = guardar_dado(rolados, guardados, indice)

            elif escolha == "2":
                print("Digite o índice do dado a ser removido (0 a 4):")
                indice = int(input())
                if 0 <= indice < len(guardados):
                    rolados, guardados = remover_dado(rolados, guardados, indice)

            elif escolha == "3":
                if contador_rerrolagens >= 2:
                    print("Você já usou todas as rerrolagens.")
                else:
                    rolados = rolar(guardados)
                    contador_rerrolagens += 1

            elif escolha == "4":
                imprime_cartela(pontuacao)

            elif escolha == "0":
                print("Digite a combinação desejada:")
                while True:
                    categoria = input()

                    if categoria in ["1","2","3","4","5","6"]:
                        if pontuacao['regra_simples'][int(categoria)] != -1:
                            print("Essa combinação já foi utilizada.")
                        else:
                            break

                    elif categoria in pontuacao['regra_avancada']:
                        if pontuacao['regra_avancada'][categoria] != -1:
                            print("Essa combinação já foi utilizada.")
                        else:
                            break

                    else:
                        print("Combinação inválida. Tente novamente.")

                pontuacao = faz_jogada(rolados + guardados, categoria, pontuacao)
                break

            else:
                print("Opção inválida. Tente novamente.")
                mostrar_menu = False

    imprime_cartela(pontuacao)

    soma_final = sum(p for p in pontuacao['regra_simples'].values() if p != -1) + \
                 sum(p for p in pontuacao['regra_avancada'].values() if p != -1)

    if sum(p for p in pontuacao['regra_simples'].values() if p != -1) >= 63:
        soma_final += 35

    print("Pontuação total:", soma_final)


jogo()
