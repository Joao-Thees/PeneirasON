"""Peneiras On - CLI (Sprint 3 / CTWP).

Arquivo principal: monta o header, o login e as rotas, integrando os modulos
jogador, olheiro e gestora. Os dados e o estilo (borda Rich) ficam em dados.py.
"""

import textos
import dados
import jogador
import olheiro
import gestora
from dados import moldura

# HEADER
# fugimos do "digite 1 para isso, 2 para aquilo": validamos o texto da rota
def header():
    """Menu inicial: le a rota e repete ate vir uma valida (ou 'sair').

    retorno (str): a rota escolhida, em minusculo, ou 'sair'.
    """
    validas = ('como funciona', 'sobre', 'faq', 'politica de privacidade',
               'entrar', 'inscricao', 'quero me inscrever', 'perfil',
               'olheiro', 'academia', 'gestora', 'feed', 'peneiras')
    moldura('COMO FUNCIONA - SOBRE - FAQ - POLITICA DE PRIVACIDADE\n'
            'ENTRAR - FEED - PENEIRAS - PERFIL - OLHEIRO - GESTORA - QUERO ME INSCREVER', 'PENEIRAS ON')
    while True:
        rota = input('rota> ').strip().lower()
        if rota == 'sair':
            return 'sair'
        if rota in validas:
            return rota
        print('Rota invalida. Digite uma opcao do menu (ou "sair").')

rota = ''  # rota atual (atualizada no laco principal)

def como_funciona():
    """Tela institucional 'como funciona'. retorno (None)."""
    moldura(textos.COMO_FUNCIONA, 'COMO FUNCIONA')

def sobre():
    """Tela institucional 'sobre', com atalho para home ou inscricao. retorno (None)."""
    moldura(textos.SOBRE, 'SOBRE')
    while True:
        tecla = input('[H] VOLTAR A HOME  |  [I] QUERO ME INSCREVER: ').strip().upper()
        if tecla == 'H':
            return  # volta pro laco principal (que reexibe o menu)
        if tecla == 'I':
            return jogador.inscricao()
        print('Pressione apenas H ou I!')

def faq():
    """Tela de FAQ (mesmas perguntas do MVP). retorno (None)."""
    moldura(
        'A inscricao e mesmo gratuita?\n'
        '  Sim. Sempre. O plano premium so da visibilidade extra. Inscricao e gratuita - para sempre.\n\n'
        'Tenho 12 anos, posso me inscrever?\n'
        '  Sim. A faixa e 07 a 19 anos. Para menores de 18, o responsavel aceita o termo na mesma tela.\n\n'
        'Nao moro perto de uma peneira.\n'
        '  O sistema usa sua localizacao para alocar voce na peneira mais proxima com vaga,\n'
        '  e abre novas peneiras onde detecta demanda.\n\n'
        'Posso enviar videos?\n'
        '  Sim. Anexe seus videos e fotos, ou cole o link do Instagram ou YouTube no perfil.\n'
        '  Videos aumentam seu score em ate 25 pontos.',
        'FAQ - DUVIDAS QUE TODO MUNDO TEM')

def politica_de_priv():
    """Tela de politica de privacidade. retorno (None)."""
    moldura(textos.POLITICA_DE_PRIV, 'POLITICA DE PRIVACIDADE')

def pedir_email(rotulo):
    """Le um email valido (com @ e dominio), repetindo ate acertar.

    rotulo (str): o texto do prompt.
    retorno (str): o email em minusculo.
    """
    while True:
        email = input(rotulo).strip().lower()
        if '@' in email and '.' in email.split('@')[-1]:
            return email
        print('Email invalido. Precisa ter @ e dominio (ex: nome@dominio.com).')

def pedir_cpf():
    """Le um CPF valido (11 digitos, so numeros), repetindo ate acertar.

    retorno (str): o CPF com 11 digitos.
    """
    while True:
        cpf = input('CPF (11 digitos, so numeros): ').strip()
        if cpf.isdigit() and len(cpf) == 11:
            return cpf
        print('CPF invalido. Digite 11 numeros, sem pontos nem tracos.')

def pedir_senha():
    """Le uma senha nao vazia, repetindo ate acertar.

    retorno (str): a senha digitada.
    """
    while True:
        senha = input('SENHA: ').strip()
        if senha:
            return senha
        print('A senha nao pode ficar vazia.')

def login():
    """Login por perfil (J/O/A) e abre o painel correspondente.

    retorno (None): grava as credenciais em dados e chama o painel do perfil.
    """
    if rota == 'entrar':
        moldura('[J] para Jogador\n[O] para Olheiro\n[A] para Academia', 'ENTRAR')

    tecla_login = input('ENTRAR COMO - digite J / O / A: ').strip().upper()

    if tecla_login == 'A':
        dados.login_academia[0]['email'] = pedir_email('E-MAIL CORPORATIVO: ')
        dados.login_academia[1]['senha'] = pedir_senha()
        print('Login de gestor(a) da academia realizado.')
        gestora.painel_gestora()

    elif tecla_login == 'J':
        dados.login_jogador[0]['email'] = pedir_email('E-MAIL: ')
        dados.login_jogador[1]['cpf'] = pedir_cpf()
        dados.login_jogador[2]['senha'] = pedir_senha()
        jogador.tela_status(dados.login_jogador[1]['cpf'])

    elif tecla_login == 'O':
        dados.login_olheiro[0]['email'] = pedir_email('EMAIL CORPORATIVO: ')
        dados.login_olheiro[1]['senha'] = pedir_senha()
        print('Login de olheiro realizado.')
        olheiro.painel_olheiro()

    else:
        print('Digite apenas J, O ou A!')
        return login()

# dicionario de rotas: cada chave (rota) aponta pra funcao que a executa
rotas_header = {"como funciona": como_funciona,
                "sobre": sobre,
                "faq": faq,
                "politica de privacidade": politica_de_priv,
                "entrar": login,
                "inscricao": jogador.inscricao,
                "quero me inscrever": jogador.inscricao,
                "perfil": jogador.perfil,
                "olheiro": olheiro.painel_olheiro,
                "academia": gestora.painel_gestora,
                "gestora": gestora.painel_gestora,
                "feed": jogador.feed,
                "peneiras": jogador.peneiras}

def principal():
    """Laco principal: mostra o menu, le a rota e despacha ate o usuario sair.

    retorno (None): roda o programa inteiro.
    """
    global rota
    while True:
        rota = header()
        if rota == 'sair':
            print('Ate mais!')
            break
        elif rota in rotas_header:
            rotas_header[rota]()  # chama a funcao da rota escolhida
        else:
            print('Error 404')

if __name__ == '__main__':
    principal()
