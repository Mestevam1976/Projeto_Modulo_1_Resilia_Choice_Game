import formatacao, ascii_imagens, funcoes

cor_erro = "red"
cor_principal = "blue"
cor_alerta = 'yellow'
cor_sucesso = 'green'

def boas_vindas():  # Exibe a mensagem inicial do jogo
    print('A Indústrias ACME produzem uma grande variedade de equipamentos e de'
          '\nbugigangas elétricas e, como tal, possui vários riscos associados' 
          '\nem seu processo produtivo.')
    print(' ')
    print('Ela possui 3 funcionários polivalentes, responsáveis pela operação,'
          '\nmanutenção e qualidade de seus equipamentos e instalações'
          '\nmas, eles são muito resistentes as boas práticas de segurança no trabalho,'
          '\ne tal resistência acaba gerando consequências indesejáveis.')
    print(' ')
    print('Pois bem, cabe a você prezado usuário decidir sobre as escolhas desses'
          '\nfuncionários e sofrer com eles as consequências dessas escolhas!')

def escolha_personagem():  # Exibe mensagem na segunda tela do jogo
    right_arrow = formatacao.escolher_cor(cor_principal, '--->')
    titulo = formatacao.escolher_cor(cor_alerta, '***** Escolha um dos três funcionários abaixo: *****' )
    print(titulo)
    formatacao.forma_linha()
    print(''
          + right_arrow + ' Gambi Harra - o mecânico - letra "A"'
          '\n'
          + right_arrow + ' Faísca - o eletricista - letra "B"'
          '\n'
          + right_arrow + ' Zé Paulada - o ajudante geral - letra "C"')
    formatacao.forma_linha()

def check_ok():
      print(ascii_imagens.check)

def mensagem_erro(): # Informa ao usuários quais letras devem ser digitadas
    texto = 'Digite corretamente apenas letras S ou N!'
    return formatacao.escolher_cor(cor_alerta, texto)

def personagem_escolhido(personagem): # Informa qual o personagem foi escolhido
    return f"O funcionário escolhido foi o sr. {formatacao.escolher_cor(cor_sucesso, personagem)}"
  

##################### DEFINIÇÕES DAS MENSAGENS PARA OS PERSONAGENS #############################

#### PERSONAGEM UM ####
def pergunta_persona_um_fase1():
      funcoes.clear()
      print('=' * 60)
      print('Você foi chamado para trocar o selo mecânico de um reator, nesse caso, o que você deve fazer?')
      formatacao.p()
      print('[A] Aplica o Lockout e/ou Tagout')
      print('[B] Realiza a manutenção imediata no equipamento'
      '\n')

def resposta_errada_fase1():
      print('''\033[91m
      Oh não!!! 
      Você escolheu a resposta errada e como consequência você poderá
      sofrer um acidente grave ou até fatal se o equipamento for ligado com você dentro dele.
      É mandatório em equipamentos rotativos o bloqueio funcional, seja elétrico ou mecânico, 
      bem como a correta identificação nos dispositivos de bloqueio de que o equipamento está em
      manutenção.''')
      print(ascii_imagens.game_over2)
                                   
def pergunta_persona_um_fase2():
      funcoes.clear()
      print('=' * 60)
      print('Essa é a Fase 2: ')
      print('Você se prepara para entrar no reator, o que é necessário agora? ')
      formatacao.p()
      print('[A] Não é necessário mais nada, devo iniciar imediatamente!')
      print('[B] Devo preencher a Permissão para Trabalho Perigoso (PTP)'
      '\n')

def resposta_errada_fase2():
      print('''\033[91m
      Essa não!
      Você escolheu a resposta errada, apesar de parecer sem importância, o preenchimento
      da Permissão de Trabalho Perigoso (PTP) é obrigatória para documentar os envolvidos
      em um serviço em que haja risco de acidente, em especial em espaços confinados como é
      o caso do interior desse reator.''')
      print(ascii_imagens.game_over2)

def pergunta_persona_um_fase3():
      funcoes.clear()
      print('=' * 60)
      print('Essa é a Fase 3: ')
      print('Você precisa entrar dentro do reator para executar a manutenção corretiva, então você: ')
      formatacao.p()
      print('[A] Começa a trabalhar imediatamente no equipamento')
      print('[B] Verifica os níveis de concentração de oxigênio e gases explosivos'
      '\n')

def resposta_errada_fase3():
      print('''\033[91m
      Escolha errada!
      Reatores, misturadores ou outros vasos de processo podem reter sobras de produtos ou
      possuírem atmosferas explosivas ou tóxicas, a medição da qualidade do ar interno dos
      equipamentos é imprescindível para o bem estar dos mantenedores desses equipamentos.''')
      print(ascii_imagens.game_over2)

#### PERSONAGEM DOIS ####
def pergunta_persona_dois_fase1():
      funcoes.clear()
      print('=' * 60)
      print('Você recebeu dois chamados para atendimento emergencial, qual deles você irá atender? ')
      print('')
      print('[A] Rearmar Cabine Primária após desarme em um temporal') # Vai para a pergunta fase 2
      print('[B] Troca do disjuntor principal do Quadro de Distribuição (QDG) do Escritório ') # Vai pergunta fase 2A

def pergunta_persona_dois_fase2():
      funcoes.clear()
      print('=' * 60)
      print('Essa é a Fase 2: ')
      print('Antes de entrar na cabine primária o que deve ser verificado?')
      print('')
      print('[A] Verificar a presença de tensão na rede elétrica')
      print('''[B] Verificar se existem equipamentos que estavam ligados no momento da queda de energia e\n    que a volta da energia pode proporcionar algum risco de operação''')
      print('''[C] Se EPI's, como Luva de Alta Tensão, a Balaclava para eletricista, o Tapete de borracha e\n    a alavanca de manobras estão presentes. ''')
      print('[D] Todas as anteriores')

def p2_resposta_errada_fase2():
      print('''\033[91m
      Oh não!!! 
      É mandatório verificar a presença da tensão elétrica na rede elétrica, um descuido com esse item é fatal;
      Também faz se necessário verificar se equipamentos que ligam automaticamente com a presença de energia, foram
      desligados, bloqueados ou se não oferecerão riscos aos operadores quando postos em funcionamento novamente.
      As cabines primárias operam com alta tensão, ou seja, acima de 1000 Volts e, tal operação exige o uso 
      adequado dos seguintes EPIs: luva de alta tensão, balaclava para eletricista, tapete de borracha e a alavanca
      isolante de manobras.
      Portanto, a resposta correta era a letra D''')
      print(ascii_imagens.game_over2)

def pergunta_persona_dois_fase2A():
      funcoes.clear()
      print('=' * 60)
      print('Essa é a Fase 2A: ')
      print('O disjuntor principal está em um painel que está energizado, o que deve ser feito primeiro?')
      print('')
      print('[A] Comunicar os setores e/ou áreas envolvidas sobre o desligamento do painel em que está o disjuntor.')
      print('[B] Checar a tensão elétrica no painel e providenciar um extintor de espuma.')
      print('[C] Após realizar o especificado na alternativa "A", providenciar o desligamento do painel que está energizado.')
      print('[D] Após realizar o especificado na alternativa "B", providenciar a remoção do disjuntor com uma chave de fenda.')
      print(' ')

def p2_resposta_errada_fase2A():
      print('''\033[91m
      Ops! Está errado!! 
      Você tem sim que comunicar aos setores e/ou áreas envolvidas que dependem do painel ligado mas, também
      deve após esse procedimento realizar o desligamento do painel antes da manutenção corretiva.
      Em hipótese alguma deve ser utilizado um extintor de espuma para combater incêndios com eletricidade!!
      A resposta correta era a letra C''')
      print(ascii_imagens.game_over2)

def pergunta_persona_dois_fase3():
      funcoes.clear()
      print('=' * 60)
      print('Essa é a Fase 3: ')
      print('Após você realizar o rearme da cabine primária o que mais precisa ser feito? ')
      print('')
      print('[A] Você registra a intervenção corretiva na Ata de Reunião.')
      print('[B] Você mede a pressão barométrica da cabine primária.')
      print('[C] Você desarma e rearma a cabine algumas vezes para ter certeza de que está tudo ok.')
      print('[D] Nenhuma das anteriores.')
      print(' ')

def p2_resposta_errada_fase3():
      print('''\033[91m
      Oh não!!! 
      Você deverá registrar sim a intervenção, como reza a NR-10, no Prontuário da Cabine e não Ata de Reunião...
      Para checar o funcionamento adequado da cabine, você deverá medir parâmetros elétricos, como tensão, 
      corrente elétrica ou potência. Pressão barométrica não faz parte das grandezas medidas em uma cabine primária.
      Apenas o rearme é suficiente, causar novos desarmes para verificar o funcionamento pode reduzir 
      a vida útil da seccionadora primária, bem como, danificar transformadores com picos de tensão desnecessários.
      A resposta correta é a letra D.''')
      print(ascii_imagens.game_over2)

def pergunta_persona_dois_fase3A():
      funcoes.clear()
      print('=' * 60)
      print('Essa é a Fase 3A: ')
      print('Ok disjuntor danificado removido, o que mais precisa ser verificado antes da instalação do novo?')
      formatacao.p()
      print('[A] As alternativas C e D estão corretas')
      print('[B] Verificar se pode ser substituído por fusíveis ultra-rápidos. ')
      print('[C] Checar e reapertar as conexões elétricas dos outros componentes do painel.')
      print('[D] Verificar o estado dos barramentos e, se necessário substituí-los também.')
      print(' ')

def p2_resposta_errada_fase3A():
      print('''\033[91m
      Eita! Você errou!! 
      Fusíveis são desaconselhados de serem utilizados em painéis elétricos modernos.
      Tendo a oportunidade de desligar o painel, o mais coerente a fazer é checar todos os itens desse painel e
      reapertar todas as conexões elétricas.
      Assim como, providenciar a substituição de componentes avariados, como por exemplo, os barramentos.
      A resposta correta é a letra  A''')
      print(ascii_imagens.game_over2)

#### PERSONAGEM TRES ####
def pergunta_persona_tres_fase1():
      funcoes.clear()
      print('=' * 60)
      print('''
      A Indústria ACME está implantando o conceito de MPT - Manutenção Produtiva Total e
      visando a adoção dessa filosofia na empresa treinou seu único operador para realizá-lo. 
      Mas, será que ele se recorda de todo treinamento?
      No caso de uma mangueira de resfriamento de molde se soltar o que ele deve fazer?''')
      formatacao.p()
      print('[A] Não faz nada e continua trabalhando normalmente, afinal é só água vazando... ')
      print('[B] Desliga o equipamento, fecha o registro correspondente ao resfriamento e verifica se pode intervir.')
      print('[C] Buscando ser proativo, ele tenta trocar a mangueira danificada com o equipamento funcionando.')
      print('[D] Pára o equipamento e vai fumar, afinal ele não é mecânico.')
      print(' ')

def p3_resposta_errada_fase1():
      print('''\033[91m
      Ops! Assim não Sr. Paulada!!
      Sair para fumar vai te causar muitos problemas!!
      A água é de resfriamento do molde, se não for reestabelecido esse resfriamento, as peças injetadas serão
      perdidas e além da água, matéria prima, insumos e eletricidades serão desperdiçados!
      Injetoras são até hoje os equipamentos que mais amputam membros na indústria mundial, fazer a troca da
      mangueira com o equipamento ligado é imprudência demais e não deve ser tentado jamais!
      O correto a fazer é parar o equipamento, fechar o registro do resfriamento e substituir a mangueira caso tenha
      confiança e segurança em fazer esse serviço, caso não se sinta a vontade, acione a manutenção. 
      Logo, a resposta correta é a letra B''')
      print(ascii_imagens.game_over2)


def pergunta_persona_tres_fase2():
      funcoes.clear()
      print('=' * 60)
      print('Essa é a Fase 2: ')
      print('A prensa Injetora em que está trabalhando apresenta um novo problema: está com ruídos excessivos. O que devo fazer? ')
      formatacao.p()
      print('[A] Nada, apesar do barulho o equipamento está funcionando corretamente.')
      print('[B] Devo procurar a origem do ruído, afinal, agora sou um operador treinado em MPT!')
      print('[C] Devo chamar o mecânico para avaliar o equipamento, afinal, excede o que aprendi no treinamento de MPT.')
      print('[D] Parar o equipamento e esperar esfriar, quem sabe resolve não?')
      print(' ')

def p3_resposta_errada_fase2():
      print('''\033[91m
      Alternativa errada!!
      Ruídos são sinais de atrito e de desgaste, não fazer nada pode comprometer o equipamento.
      Procurar a origem do ruído pode ser perigoso, uma vez que máquina só faz barulho em 
      funcionamento, o que pode ser arriscado e o treinamento de MPT não prevê manutenção profunda.
      Dificilmente ruídos cessam sozinhos, quando isso ocorre é sinal de desgaste excessivo.
      A resposta correta é a letra C, a melhor opção nesses casos é chamar um mecânico.''')
      print(ascii_imagens.game_over2)

def pergunta_persona_tres_fase3():
      funcoes.clear()
      print('=' * 60)
      print('Essa é a Fase 3: ')
      print('''
      O local de trabalho está bem bagunçado, materiais espalhados pelo chão, em cima das mesas e cadeiras,
      fora que as ferramentas de trabalho estão dispersas em toda fábrica, o que poderia ser feito?''')
      formatacao.p()
      print('[A] Limpar a seção, organizar as ferramentas e catalogar os materiais de trabalho.')
      print('[B] Pedir ajuda ao pessoal da manutenção para organizar o ambiente.')
      print('[C] Pedir ao proprietário um aumento de salário pelos serviços adicionais.')
      print('[D] Não fazer nada, está como está.')
      print(' ')

def p3_resposta_errada_fase3():
      print('''\033[91m
      Você errou!!
      Um dos focos do MPT é a ambiente de trabalho e, ele deve ser limpo, organizado e acessível para o operador.
      Isso é de responsabilidade do operador e de mais ninguém.
      O aumento de salário não deveria ser uma moeda de barganha e sim um benefício recebido pelo mérito.
      A resposta correta é a letra A''')
      print(ascii_imagens.game_over2)

###################################################################################################
def inicia_jogo():
      print('Ok vamos começar!')
   