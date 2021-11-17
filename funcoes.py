from os import system, name  # importa informações sobre o sistema operacional em uso
import formatacao  # importa as funções do arquivo 'formatacao.py'
import mensagens  # importa as funções do arquivo 'mensagens.py'
import ascii_imagens

def clear():  # Limpa a tela removendo do prompt as informações sobre a localização dos arquivos
  # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def sai_do_jogo():  # Encerra o aplicativo e volta ao prompt de comando
    exit()

def jogar():  # Dá a opção para o usuário continuar no jogo ou sair
    letra_S = False

    while letra_S == False:
        formatacao.forma_linha()
        joga = input('\033[92m Deseja continuar? Digite S para Sim ou N para sair do jogo: \033[0m')
        formatacao.forma_linha()
        if joga == 'S' or joga == 's':
            letra_S = True
            pass
        elif joga == 'N' or joga == 'n':
            sai_do_jogo()
        else:
            print(mensagens.mensagem_erro())
            letra_S = False

def entrada():  # Coleta do usuário a entrada para escolha do personagem
    
    seletor = 0
    atende = False

    while atende == False:
        escolha = input('Por favor, escolha um dos personagens acima (letra A, B ou C): ')

        if escolha == 'A' or escolha == 'a':
            personagem = 'Gambi Harra'
            atende = True
            seletor = 1

        elif escolha == 'B' or escolha == 'b':
            personagem = 'Faísca'
            atende = True
            seletor = 2

        elif escolha == 'C' or escolha == 'c':
            personagem = 'Zé Paulada'
            atende = True
            seletor = 3

        else:
            mensagem_erro = 'Digite corretamente apenas letras A, B ou C!'
            print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))

        if(atende == True):
            formatacao.forma_linha()
            print(mensagens.personagem_escolhido(personagem))
            formatacao.forma_linha()
            confirma = input('''\nTudo bem? 
            \nÉ com esse personagem que vai jogar? 
            \nDigite S para confirmar.
            \nOu qualquer letra para escolher outro personagem: ''')
            if confirma == 'S' or confirma == 's':
                if seletor == 1:
                    caminho_personagem1()
                elif seletor == 2:
                    caminho_personagem2()
                elif seletor == 3:
                    caminho_personagem3()
            else:
                clear()
                mensagens.escolha_personagem()
                entrada()

def reinicio(): # Em caso de game over retorna ao menu principal ou sai do jogo
    texto = 'Deseja jogar novamente? Digite S para continuar ou tecle Enter para encerrar: '
    formatacao.forma_linha()
    reinicia = input(formatacao.escolher_cor('yellow', texto))
    if reinicia == 'S' or reinicia == 's':
        clear()
        mensagens.escolha_personagem()
        entrada()
    else:
        sai_do_jogo()
        
def caminho_personagem1():  # Inicia o jogo com o caminho para o personagem 1
    def fase_tres():
        mensagens.pergunta_persona_um_fase3()
        resposta = False

        while resposta == False:
            final_fase3 = input('Digite A ou B para informar sua decisão: ')

            if final_fase3 == 'A' or final_fase3 == 'a':
                mensagens.resposta_errada_fase3()
                resposta = True
                reinicio()

            elif final_fase3 == 'B' or final_fase3 == 'b':
                clear()
                escolha_certa = (('=')*60 +
                                 '\n' + (' ' * 25) + 'PARABÉNS!!!'
                                 '\n' + (' ' * 15) +
                                 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                                 '\n' + (' ' * 22) + 'VOCÊ GANHOU O JOGO!!!!'
                                 '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                print(ascii_imagens.vencedor)
                reinicio()
                resposta = True
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False

    def fase_dois():
        mensagens.pergunta_persona_um_fase2()
        resposta = False

        while resposta == False:
            final_fase2 = input('Digite A ou B para informar sua decisão: ')

            if final_fase2 == 'A' or final_fase2 == 'a':
                mensagens.resposta_errada_fase2()
                resposta = True
                reinicio()

            elif final_fase2 == 'B' or final_fase2 == 'b':
                clear()
                mensagens.check_ok()
                escolha_certa = (('=')*60 +
                                 '\n' + (' ' * 25) + 'PARABÉNS!!!'
                                 '\n' + (' ' * 15) +
                                 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                                 '\n' + (' ' * 10) +
                                 'O PREENCHIMENTO DA PTP É OBRIGATÓRIO E ASSEGURA '
                                 '\n' + (' ' * 10) +
                                 'QUE TODAS AS ÁREAS SEJAM INFORMADAS DO SERVIÇO. '
                                 '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                loop_erro = False
                while loop_erro == False:
                    continua = input('Digite S para continuar para a fase 3: ')
                    if continua == 'S' or continua == 's':
                        loop_erro = True
                        fase_tres()
                    else:
                        print(formatacao.escolher_cor(mensagens.cor_alerta,'Digite somente S para continuar!'))
                        loop_erro = False
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False
                
            
    def fase_um():
        mensagens.pergunta_persona_um_fase1()
        resposta = False

        while resposta == False:
            final_fase1 = input('Digite A ou B para informar sua decisão: ')

            if final_fase1 == 'B' or final_fase1 == 'b':
                mensagens.resposta_errada_fase1()
                resposta = True
                reinicio()

            elif final_fase1 == 'A' or final_fase1 == 'a':
                clear()
                mensagens.check_ok()
                escolha_certa = (('=')*60 +
                                 '\n' + (' ' * 25) + 'PARABÉNS!!!'
                                 '\n' + (' ' * 15) +
                                 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                                 '\n' + (' ' * 10) +
                                 'O BLOQUEIO ELÉTRICO E/OU MECÂNICO DO EQUIPAMENTO '
                                 '\n' + (' ' * 10) +
                                 'E A CORRETA IDENTIFICAÇÃO SÃO IMPRESCINDÍVEIS. '
                                 '\n' + (' ' * 10) +
                                 'VOCÊ AVANÇOU PARA A FASE 2, BOA SORTE!!!'
                                 '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                loop_erro = False
                while loop_erro == False:
                    continua = input('Digite S para continuar para a fase 2: ')
                    if continua == 'S' or continua == 's':
                        loop_erro = True
                        fase_dois()
                    else:
                        print(formatacao.escolher_cor(mensagens.cor_alerta,'Digite somente S para continuar!'))
                        loop_erro = False
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False
    fase_um()

def caminho_personagem2():  # Inicia o jogo com o caminho para o personagem 2
    def fase_tres_A():
        mensagens.pergunta_persona_dois_fase3A()

        resposta = False

        while resposta == False:
            final_fase3 = input('Digite A ou B para informar sua decisão: ')

            if final_fase3 == 'B' or final_fase3 == 'b' or final_fase3 == 'C' or\
                final_fase3 == 'c' or final_fase3 == 'D' or final_fase3 == 'd':
                mensagens.p2_resposta_errada_fase3A()
                resposta = True
                reinicio()

            elif final_fase3 == 'A' or final_fase3 == 'a':
                clear()
                escolha_certa = (('=')*60 +
                                 '\n' + (' ' * 25) + 'PARABÉNS!!! VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                                 '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                print(ascii_imagens.vencedor)
                reinicio()
            else:
                mensagem_erro = 'Digite corretamente apenas letras A, B, C ou D!'
                print(formatacao.escolher_cor(
                    mensagens.cor_alerta, mensagem_erro))
                resposta = False

    def fase_tres():
        mensagens.pergunta_persona_dois_fase3()

        resposta = False

        while resposta == False:
            final_fase3 = input('Digite A ou B para informar sua decisão: ')

            if final_fase3 == 'A' or final_fase3 == 'a' or final_fase3 == 'B'or\
                final_fase3 == 'b' or final_fase3 == 'C' or final_fase3 == 'c':
                mensagens.p2_resposta_errada_fase3()
                resposta = True
                reinicio()

            elif final_fase3 == 'D' or final_fase3 == 'd':
                clear()
                escolha_certa = (('=')*60 +
                                 '\n' + (' ' * 25) + 'PARABÉNS!!!'
                                 '\n' + (' ' * 15) +
                                 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                                 '\n' + (' ' * 22) + 'VOCÊ GANHOU O JOGO!!!!'
                                 '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                print(ascii_imagens.vencedor)
                reinicio()
            else:
                mensagem_erro = 'Digite corretamente apenas letras A, B, C ou D!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False

    def fase_dois_A():
        mensagens.pergunta_persona_dois_fase2A()

        resposta = False

        while resposta == False:
            final_fase2 = input('Digite A, B, C ou D para informar sua decisão: ')

            if final_fase2 == 'A' or final_fase2 == 'a' or final_fase2 == 'B' or \
                final_fase2 == 'b' or final_fase2 == 'D' or final_fase2 == 'd':
                mensagens.p2_resposta_errada_fase2A()
                resposta = True
                reinicio()

            elif final_fase2 == 'C' or final_fase2 == 'c':
                clear()
                mensagens.check_ok()
                escolha_certa = (('=')*60 +
                                 '\n' + (' ' * 25) + 'PARABÉNS!!!'
                                 '\n' + (' ' * 15) +
                                 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                                 '\n' + (' ' * 10) +
                                 'ANTES DE DESLIGAR O PAINÉL VOCÊ INFORMOU A'
                                 '\n' + (' ' * 10) +
                                 'TODAS AS ÁREAS ENVOLVIDAS NO PROCESSO. '
                                 '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                loop_erro = False
                while loop_erro == False:
                    continua = input('Digite S para continuar para a fase 2: ')
                    if continua == 'S' or continua == 's':
                        loop_erro = True
                        fase_tres_A()
                    else:
                        print(formatacao.escolher_cor(mensagens.cor_alerta,'Digite somente S para continuar!'))
                        loop_erro = False
                
            else:
                mensagem_erro = 'Digite corretamente apenas letras A, B, C ou D!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False

    def fase_dois():
        mensagens.pergunta_persona_dois_fase2()
        formatacao.p()
        resposta = False

        while resposta == False:
            final_fase2 = input('Digite A, B, C ou D para informar sua decisão: ')

            if final_fase2 == 'A' or final_fase2 == 'a' or final_fase2 == 'B' or \
                final_fase2 == 'b' or final_fase2 == 'C' or final_fase2 == 'c':
                mensagens.p2_resposta_errada_fase2()
                resposta = True
                reinicio()

            elif final_fase2 == 'D' or final_fase2 == 'd':
                clear()
                mensagens.check_ok()
                escolha_certa = (('=')*60 +
                                 '\n' + (' ' * 30) + 'PARABÉNS!!!'
                                 '\n' + (' ' * 15) +
                                 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                                 '\n' + (' ' * 10) +
                                 'VOCÊ DEVE VERIFICAR SE TEM TENSÃO NA REDE ELÉTRICA, '
                                 '\n' + (' ' * 5) +
                                 'SE HÁ EQUIPAMENTOS LIGADOS E QUE PODEM LIGAR AUTOMATICAMENTE '
                                '\n' + (' ' * 7) +
                                 'E SE OS EPIS ESTÃO DISPONÍVEIS PARA UTILIZAÇÃO NO SERVIÇO. '
                                 '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                loop_erro = False
                while loop_erro == False:
                    continua = input('Digite S para continuar para a fase 2: ')
                    if continua == 'S' or continua == 's':
                        loop_erro = True
                        fase_tres()
                    else:
                        print(formatacao.escolher_cor(mensagens.cor_alerta,'Digite somente S para continuar!'))
                        loop_erro = False
                
            else:
                mensagem_erro = 'Digite corretamente apenas letras A, B, C ou D!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False

    def fase_um():
        mensagens.pergunta_persona_dois_fase1()

        resposta = False

        while resposta == False:
            formatacao.p()
            final_fase1 = input('Digite A ou B para informar sua decisão: ')

            if final_fase1 == 'B' or final_fase1 == 'b':
                clear()
                escolha_certa = 'OK Você selecionou a troca do disjuntor do QDG, siga em frente com cautela: '
                print(formatacao.escolher_cor(mensagens.cor_erro, escolha_certa))
                resposta = True
                formatacao.forma_linha()
                loop_erro = False
                while loop_erro == False:
                    continua = input('Digite S para continuar para a fase 2A: ')
                    if continua == 'S' or continua == 's':
                        loop_erro = True
                        fase_dois_A()
                    else:
                        print(formatacao.escolher_cor(mensagens.cor_alerta,'Digite somente S para continuar!'))
                        loop_erro = False
                                
            elif final_fase1 == 'A' or final_fase1 == 'a':
                clear()
                escolha_certa = 'OK Você selecionou o rearme da cabine primária, siga em frente'
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                formatacao.forma_linha()
                loop_erro = False
                while loop_erro == False:
                    continua = input('Digite S para continuar para a fase 2: ')
                    if continua == 'S' or continua == 's':
                        loop_erro = True
                        fase_dois()
                    else:
                        print(formatacao.escolher_cor(mensagens.cor_alerta,'Digite somente S para continuar!'))
                        loop_erro = False
            
            else:
                mensagem_erro = 'Digite corretamente apenas letras A ou B!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False
    fase_um()

def caminho_personagem3():  # Inicia o jogo com o caminho para o personagem 3
    def fase_tres():
        mensagens.pergunta_persona_tres_fase3()

        resposta = False

        while resposta == False:
            final_fase3 = input('Digite A, B, C ou D para informar sua decisão: ')

            if final_fase3 == 'B' or final_fase3 == 'b' or final_fase3 == 'C' or\
                final_fase3 == 'c' or final_fase3 == 'D' or final_fase3 == 'd':
                mensagens.p3_resposta_errada_fase3()
                resposta = True
                reinicio()

            elif final_fase3 == 'A' or final_fase3 == 'a':
                escolha_certa = (('=')*60 +
                                 '\n' + (' ' * 25) + 'PARABÉNS!!!'
                                 '\n' + (' ' * 15) +
                                 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                                 '\n' + (' ' * 22) + 'VOCÊ GANHOU O JOGO!!!!'
                                 '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                print(ascii_imagens.vencedor)
                reinicio()
            else:
                mensagem_erro = 'Digite corretamente apenas letras A, B, C ou D!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False

    def fase_dois():
        mensagens.pergunta_persona_tres_fase2()

        resposta = False

        while resposta == False:
            final_fase2 = input('Digite A, B, C ou D para informar sua decisão: ')

            if final_fase2 == 'A' or final_fase2 == 'a' or final_fase2 == 'B' or\
                final_fase2 == 'b' or final_fase2 == 'D' or final_fase2 == 'd':
                mensagens.p3_resposta_errada_fase2()
                resposta = True
                reinicio()

            elif final_fase2 == 'C' or final_fase2 == 'c':
                clear()
                mensagens.check_ok()
                escolha_certa = (('=')*60 +
                                 '\n' + (' ' * 25) + 'PARABÉNS!!!'
                                 '\n' + (' ' * 15) +
                                 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                                 '\n'
                                 + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                loop_erro = False
                while loop_erro == False:
                    continua = input('Digite S para continuar para a fase 3: ')
                    if continua == 'S' or continua == 's':
                        loop_erro = True
                        fase_tres()
                    else:
                        print(formatacao.escolher_cor(mensagens.cor_alerta,'Digite somente S para continuar!'))
                        loop_erro = False
                
            else:
                mensagem_erro = 'Digite corretamente apenas letras A, B, C ou D!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False

    def fase_um():
        mensagens.pergunta_persona_tres_fase1()

        resposta = False

        while resposta == False:
            final_fase1 = input('Digite A, B, C ou D para informar sua decisão: ')

            if final_fase1 == 'A' or final_fase1 == 'a' or final_fase1 == 'C' or\
                final_fase1 == 'c' or final_fase1 == 'D' or final_fase1 == 'd':
                mensagens.p3_resposta_errada_fase1()
                resposta = True
                reinicio()

            elif final_fase1 == 'B' or final_fase1 == 'b':
                clear()
                mensagens.check_ok()
                escolha_certa = (('=')*60 +
                                 '\n' + (' ' * 25) + 'PARABÉNS!!!'
                                 '\n' + (' ' * 15) +
                                 'VOCÊ ESCOLHEU A RESPOSTA CORRETA!!!'
                                 '\n' + (' ' * 10) +
                                 'VOCÊ AVANÇOU PARA A FASE 2, BOA SORTE!!!'
                                 '\n' + ('=')*60)
                print(formatacao.escolher_cor(mensagens.cor_sucesso, escolha_certa))
                resposta = True
                loop_erro = False
                while loop_erro == False:
                    continua = input('Digite S para continuar para a fase 2: ')
                    if continua == 'S' or continua == 's':
                        loop_erro = True
                        fase_dois()
                    else:
                        print(formatacao.escolher_cor(mensagens.cor_alerta,'Digite somente S para continuar!'))
                        loop_erro = False
                
            else:
                mensagem_erro = 'Digite corretamente apenas letras A, B, C ou D!'
                print(formatacao.escolher_cor(mensagens.cor_alerta, mensagem_erro))
                resposta = False
    fase_um()
