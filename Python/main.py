import textos
from datetime import datetime, date

# site para correção: peneirason.vercel.app

IDADE_MIN = 7
IDADE_MAX = 19

ESTADOS = {'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 
           'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 
           'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'}

POSICOES = {'GOLEIRO', 'ZAGUEIRO', 'LATERAL', 'VOLTANTE', 'MEIA', 'PONTA', 'ATACANTE'}

PE_DOMINANTE = {'DIREITO', 'ESQUERDO', 'AMBIDESTRO'}

# HEADER
# começando por inputs, queremos fugir do tradicional "Insira 1 para isso e 2 para aquilo" Focamos em validar inputs
def header():

    print('PENEIRAS ON - COMO FUNCIONA - SOBRE - FAQ - POLÍTICA DE PRIVACIDADE - ENTRAR - QUERO ME INSCREVER')
    while True:

        rota = input('rota> ').strip().lower()
        if rota == "sair".strip().lower():
            break
        return rota

rota = header()
def como_funciona():
        print(textos.COMO_FUNCIONA)
def sobre():

    print(textos.SOBRE)
    tecla = input('VOLTAR A HOME - QUERO ME INSCREVER [PRESSIONE H PARA HOME OU I PARA INSCRIÇÃO]: ')
    if tecla.strip().upper() == 'H': 
        return header()
    elif tecla.strip().upper() == 'I':
        return inscricao()
    else:
        try:
            print('PRESSIONE APENAS I OU H!')
        except:
            header()

def inscricao():

    print('QUEM É VOCE?')
    nome_completo = input('Seu Nome Completo: ')
    
    while True:
        try:
            data_de_nascimento = input('DD/MM/YYYY: ')
            data_de_nascimento = datetime.strptime(data_de_nascimento, "%d/%m/%Y")
            hoje = date.today()
            idade = hoje.year - data_de_nascimento.year

            if (hoje.month, hoje.day) < (data_de_nascimento.month, data_de_nascimento.day):
                idade -= 1 # verificando caso o usuario faca idade no messmo 

            if idade < IDADE_MIN or idade > IDADE_MAX: # or
                print(f'Idade fora da faixa permitida (07-19). Você tem {idade}.')   
            else:
                break  

        except ValueError:
            print("Data inválida! Digite Novamente.")

    while True:
        try:
            cpf = input('CPF - 11 dígitos - SOMENTE NÚMEROS: ').strip().upper()

            if not cpf.isdigit() or len(cpf) != 11:
                print('Digite um CPF Válido!')   # inválido -> while repete sozinho
            else:
                break                             # válido -> sai do loop e segue

        except ValueError:
            print('CPF Inválido! Digite um CPF Válido!')

    while True:

        try:
            estado = input('ESTADO: ').strip().upper()
            cidade = input('SUA CIDADE: ').strip().upper()
            # O front end não tem validação de cidade válida (só tem validação de formulario), por isso não tem aqui
            if estado not in ESTADOS:
                print('Informe o Estado aonde voce mora.')
            elif not cidade: # no front so tem validação de campo vazio (validacao de formularios)
                print('Informe a cidade onde voce mora.')
            else:
                break

        except ValueError:
            print('Cidade ou Estado Inválidos!')

    while True:

        try:
            print('COMO VOCE JOGA?')
            posicoes = str(input(f'Selecione uma das posições disponíveis: {POSICOES}')).strip().upper()
            pe_dominante = str(input('PÉ DOMINANTE: ')).strip().upper()
            altura = float(input('ALTURA (CM): '))
            peso = float(input('PESO (KG):'))
            onde_joga = input('NOME DA ESCOLA OU CLUBE AONDE VOCE JOGA: ')
            tempo_de_pratica = int(input('TEMPO DE PRATICA (ANOS): '))
            # no MVP visual NÂO há validação de altura, peso, cidade e tempo de pratica
            if posicoes not in POSICOES:
                print('Digite uma posição correta!')
            elif pe_dominante not in PE_DOMINANTE:
                print('Digite um pé dominante correto!')
            else:
                break

        except ValueError:
            print('Posição Inválida ou Pé Dominante inválidos!')

        
    print('MÍDIAS (opcional - dê Enter para pular)')
    
    # link de vídeo do YouTube/Instagram: só uma string, sem validação travando
    video = input('Link do seu vídeo (YouTube/Instagram): ').strip()

    # foto: caminho do arquivo local ou URL. também é só texto
    foto = input('Caminho ou link da sua foto: ').strip()
        
    # PASSO 5 - RESPONSÁVEL (condicional: só menor de 18)
    if idade >= 18:
        print('VOCE É MAIOR. SEM NECESSIDADE DE RESPONSÁVEL, CONFIRME SUA INSCRIÇÃO E PRESSIONE ENTER')
        nome_responsavel = ''
        telefone_responsavel = ''
        aceite = ''
    else:
        # nome do responsável: repete enquanto vier vazio
        nome_responsavel = input('Nome Completo do Responsável: ').strip()
        while not nome_responsavel:
            print('Informe o nome completo do responsável legal.')
            nome_responsavel = input('Nome Completo do Responsável: ').strip()

        telefone_responsavel = input('CELULAR DO RESPONSÁVEL (só números, com DDD): ').strip()
        while not telefone_responsavel.isdigit():
            print('Digite o Celular com DDD, apenas números.')
            telefone_responsavel = input('CELULAR DO RESPONSÁVEL (só números, com DDD): ').strip()

        aceite = input('ACEITO O TERMO RESPONSÁVEL? [S/N] ').strip().upper()
        while aceite not in ('S', 'N'):
            print('Digite apenas S ou N!')
            aceite = input('ACEITO O TERMO RESPONSÁVEL? [S/N] ').strip().upper()

        if aceite == 'N':
            print('Sem o aceite do responsável não é possível concluir a inscrição.')
            return header()
    atleta = {
        'nome': nome_completo,
        'nascimento': data_de_nascimento, # objeto datetime -> formatar com strftime ao exibir
        'idade': idade,
        'cpf': cpf,
        'uf': estado,
        'cidade': cidade,
        'posicao': posicoes,
        'pe': pe_dominante,
        'altura': altura,
        'peso': peso,
        'clube': onde_joga,
        'anos_pratica': tempo_de_pratica,
        'video': video,
        'foto': foto,
        'responsavel': nome_responsavel,
        'tel_responsavel': telefone_responsavel,
        'aceite_termo': aceite,
        'atributos': {}, # 8 atributos técnicos: preenchidos depois (tela perfil)
        'score': 0, # score de completude: calculado depois
    }
    atletas.append(atleta) 

    input('APERTE ENTER PARA CONFIRMAR A INSCRIÇÃO! ')
    print('''Inscrição enviada \n
            Perfil criado. \n
            Você está no jogo. \n

            Seu perfil foi registrado. Você recebe SMS com a confirmação e será alocado na peneira mais próxima com vaga.''')

    return login()

def feed():

    print(textos.FEED)
    print(POSICOES)

    posicoes_feed = input('POSIÇÃO (Enter para todas): ').strip().upper()
    while posicoes_feed and posicoes_feed not in POSICOES:
        print('Posição inválida! Escolha uma da lista ou dê Enter para todas.')
        posicoes_feed = input('POSIÇÃO (Enter para todas): ').strip().upper()

    estado_feed = input('ESTADO (Enter para todos): ').strip().upper()
    while estado_feed and estado_feed not in ESTADOS:
        print('Estado inválido! Use a sigla (ex: RJ) ou dê Enter para todos.')
        estado_feed = input('ESTADO (Enter para todos): ').strip().upper()

    filtrados = []
    for a in atletas:
        if posicoes_feed and a['posicao'] != posicoes_feed:
            continue
        if estado_feed and a['uf'] != estado_feed:
            continue
        filtrados.append(a)

    if not filtrados:
        print('Nenhum atleta com esses filtros. Tente outra posição ou outro estado.')
        return

    for a in filtrados:
        print(f"{a['nome']} | {a['posicao']} | {a['cidade']}/{a['uf']} | {a['idade']} anos | score {a['score']}")

# criar funcao separada para limpar filtros

                

                


    




    


def faq():
    print('''FAQ
            Dúvidas que todo mundo tem.
            A inscrição é mesmo gratuita?
            +
            Sim. Sempre. O plano premium só dá visibilidade extra. Inscrição é gratuita — para sempre.

            Tenho 12 anos, posso me inscrever?
            +
            Sim. A faixa é 07 a 19 anos. Para menores de 18, o responsável aceita o termo na mesma tela.

            Não moro perto de uma peneira.
            +
            O sistema usa sua localização para alocar você na peneira mais próxima com vaga, e abre novas peneiras onde detecta demanda.

            Posso enviar vídeos?
            +
            Sim. Anexe seus vídeos e fotos, ou cole o link do Instagram ou YouTube no perfil. Vídeos aumentam seu score em até 25 pontos.''')
def politica_de_priv():
    print(textos.POLITICA_DE_PRIV)

def login():
    
    if rota == 'entrar':
        print('''JOGADOR
                OLHEIRO
                ACADEMIA
                
                Aperte: 
                [CNTRL + J] para Jogador
                [CNTRL + O] para Olheiro
                [CNTRL + A] para Academia''')
    tecla_login = msvcrt.getch()

    if tecla_login == b'\x01': # letra A

        cadastro_academia_email = input('E-MAIL CORPORATIVO: ').strip().lower() 
        academia[0]['email'] = cadastro_academia_email

        cadastro_academia_senha = input('SENHA: ').strip().lower()
        academia[1]['senha'] = cadastro_academia_senha

    elif tecla_login == b'\n': # Letra J

        cadastro_jogador_email = input('E-MAIL: ')
        jogador[0]['email'] = cadastro_jogador_email

        cadastro_jogador_cpf = input('CPF: ')
        jogador[1]['cpf'] = cadastro_jogador_cpf

        cadastro_jogador_senha = input('SENHA: ')
        jogador[2]['senha'] = cadastro_jogador_senha
    
    elif tecla_login == b'\x0f': # Letra O

        cadastro_olheiro_email = input('EMAIL CORPORATIVO: ')
        olheiros[0]['email'] = cadastro_olheiro_email

        cadastro_olheiro_senha = input('SENHA: ')
        olheiros[1]['senha'] = cadastro_olheiro_senha
    else:
        try:
            print('Digite apenas os comandos ditados!')
            login()
        except KeyboardInterrupt:
            header()

rotas_header = {"como funciona": como_funciona,
                "sobre": sobre,
                "faq": faq,
                "politica de privacidade": politica_de_priv,
                "entrar": login,
                "inscricao": inscricao,
                "feed": feed}

olheiros = [{}, {}] # indice 0, indice 1
jogador = [{}, {}, {}]
academia = [{}, {}]

atletas = [] # lista de dicionários: cada dict = 1 atleta cadastrado
perfis_posicao = {}
presencas = [[]]
avaliacoes = [[]]
       
if rota in rotas_header:
    rotas_header[rota]()
else:
    print('Error 404')


