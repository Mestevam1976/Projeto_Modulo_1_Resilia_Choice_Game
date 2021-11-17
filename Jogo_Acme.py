#################################### IMPORTA FUNÇÕES ###########################################
import funcoes # importa as funções do arquivo 'funcoes.py'
import formatacao # importa as funções do arquivo 'formatacao.py'
import mensagens # importa as funções do arquivo 'mensagens.py'

#################################### CÓDIGO DO JOGO: ###########################################
funcoes.clear() # executa a função 'clear()' que está no arquivo importado 'funcoes.py'
formatacao.cabecalhoI()
mensagens.boas_vindas()
formatacao.forma_linha()
funcoes.jogar()
funcoes.clear()
formatacao.forma_linha()
mensagens.escolha_personagem()

######################### ENTRADA DE DADOS & SELEÇÃO DO PERSONAGEM: ############################
formatacao.forma_linha()
funcoes.entrada()
formatacao.forma_linha()

##################################### INÍCIO DO JOGO: ##########################################


