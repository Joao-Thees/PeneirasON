"""Dados e estilo compartilhados do Peneiras On.

Guarda as constantes, as colecoes (listas, dicionarios e matrizes) e o helper
de borda Rich. Todos os modulos (jogador, olheiro, gestora, main) importam daqui,
assim cada pedaco usa o MESMO formato de atleta/peneira e a mesma cor de borda.
"""

import sys
from datetime import datetime
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box

# garante UTF-8 na saida (Windows usa cp1252 e quebraria com ->, -, acentos)
try:
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stdin.reconfigure(encoding='utf-8')
except (AttributeError, ValueError):
    pass

# ---- estilo (borda Rich, como um border/border-radius do CSS) ----
console = Console(legacy_windows=False)  # renderizador moderno (evita erro no console antigo)
VERDE_LIMA = '#9EFF00'  # verde limao padrao da peneirason (muda so aqui)

def moldura(texto, titulo=''):
    """Imprime um bloco de texto dentro de uma borda arredondada verde-lima.

    texto (str): o conteudo a exibir.
    titulo (str): titulo opcional na borda de cima.
    retorno (None): so imprime no terminal.
    """
    # Text() faz o texto sair literal (nao interpreta [x], [ ] como marcacao Rich)
    console.print(Panel(Text(texto), title=titulo, border_style=VERDE_LIMA, box=box.ROUNDED))

# ---- constantes ----
IDADE_MIN = 7
IDADE_MAX = 19

ESTADOS = {'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
           'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
           'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'}

POSICOES = {'GOLEIRO', 'ZAGUEIRO', 'LATERAL', 'VOLANTE', 'MEIA', 'PONTA', 'ATACANTE'}

PE_DOMINANTE = {'DIREITO', 'ESQUERDO', 'AMBIDESTRO'}

# ---- credenciais de login por perfil (preenchidas no login) ----
login_olheiro = [{}, {}]      # indice 0 = email, indice 1 = senha
login_jogador = [{}, {}, {}]  # email, cpf, senha
login_academia = [{}, {}]     # email, senha

# ---- massa demo: 12 atletas (score 91 a 62, menores e maiores, com e sem video) ----
# lista de dicionarios; mesmo schema montado na inscricao (atributos = dict aninhado)
atletas = [
    {'nome': 'Kaua Ferreira', 'nascimento': datetime(2008, 3, 12), 'idade': 18, 'cpf': '11111111111',
     'uf': 'RJ', 'cidade': 'DUQUE DE CAXIAS', 'posicao': 'ATACANTE', 'pe': 'DIREITO', 'altura': 178.0, 'peso': 70.0,
     'clube': 'Base RJ', 'anos_pratica': 8, 'video': 'https://youtu.be/demo1', 'foto': 'foto1.jpg',
     'responsavel': '', 'tel_responsavel': '', 'aceite_termo': '',
     'atributos': {'velocidade': 88, 'finalizacao': 90, 'passe': 62, 'drible': 82, 'defesa': 30, 'cabeceio': 72, 'fisico': 76, 'reflexo': 55}, 'score': 91},
    {'nome': 'Miguel Santos', 'nascimento': datetime(2009, 7, 5), 'idade': 17, 'cpf': '22222222222',
     'uf': 'PE', 'cidade': 'RECIFE', 'posicao': 'MEIA', 'pe': 'ESQUERDO', 'altura': 172.0, 'peso': 65.0,
     'clube': 'Nautico Sub-17', 'anos_pratica': 7, 'video': 'https://youtu.be/demo2', 'foto': 'foto2.jpg',
     'responsavel': 'Ana Santos', 'tel_responsavel': '81999990002', 'aceite_termo': 'S',
     'atributos': {'velocidade': 74, 'finalizacao': 70, 'passe': 88, 'drible': 84, 'defesa': 45, 'cabeceio': 55, 'fisico': 66, 'reflexo': 50}, 'score': 88},
    {'nome': 'Davi Oliveira', 'nascimento': datetime(2007, 11, 20), 'idade': 18, 'cpf': '33333333333',
     'uf': 'SP', 'cidade': 'SAO PAULO', 'posicao': 'ZAGUEIRO', 'pe': 'DIREITO', 'altura': 186.0, 'peso': 80.0,
     'clube': 'Base SP', 'anos_pratica': 9, 'video': 'https://youtu.be/demo3', 'foto': 'foto3.jpg',
     'responsavel': '', 'tel_responsavel': '', 'aceite_termo': '',
     'atributos': {'velocidade': 60, 'finalizacao': 30, 'passe': 65, 'drible': 45, 'defesa': 90, 'cabeceio': 85, 'fisico': 88, 'reflexo': 55}, 'score': 85},
    {'nome': 'Arthur Lima', 'nascimento': datetime(2010, 1, 30), 'idade': 16, 'cpf': '44444444444',
     'uf': 'AM', 'cidade': 'MANAUS', 'posicao': 'PONTA', 'pe': 'ESQUERDO', 'altura': 170.0, 'peso': 63.0,
     'clube': 'Amazonas FC', 'anos_pratica': 6, 'video': 'https://youtu.be/demo4', 'foto': 'foto4.jpg',
     'responsavel': 'Marcos Lima', 'tel_responsavel': '92999990004', 'aceite_termo': 'S',
     'atributos': {'velocidade': 92, 'finalizacao': 74, 'passe': 66, 'drible': 90, 'defesa': 28, 'cabeceio': 50, 'fisico': 64, 'reflexo': 52}, 'score': 83},
    {'nome': 'Bernardo Alves', 'nascimento': datetime(2011, 5, 8), 'idade': 15, 'cpf': '55555555555',
     'uf': 'PR', 'cidade': 'CURITIBA', 'posicao': 'VOLANTE', 'pe': 'DIREITO', 'altura': 175.0, 'peso': 68.0,
     'clube': 'Base PR', 'anos_pratica': 5, 'video': '', 'foto': 'foto5.jpg',
     'responsavel': 'Julia Alves', 'tel_responsavel': '41999990005', 'aceite_termo': 'S',
     'atributos': {'velocidade': 70, 'finalizacao': 55, 'passe': 80, 'drible': 62, 'defesa': 78, 'cabeceio': 66, 'fisico': 82, 'reflexo': 50}, 'score': 80},
    {'nome': 'Heitor Costa', 'nascimento': datetime(2012, 9, 14), 'idade': 14, 'cpf': '66666666666',
     'uf': 'RJ', 'cidade': 'DUQUE DE CAXIAS', 'posicao': 'GOLEIRO', 'pe': 'DIREITO', 'altura': 180.0, 'peso': 72.0,
     'clube': 'Base RJ', 'anos_pratica': 5, 'video': 'https://youtu.be/demo6', 'foto': '',
     'responsavel': 'Paula Costa', 'tel_responsavel': '21999990006', 'aceite_termo': 'S',
     'atributos': {'velocidade': 42, 'finalizacao': 20, 'passe': 55, 'drible': 25, 'defesa': 90, 'cabeceio': 52, 'fisico': 70, 'reflexo': 95}, 'score': 78},
    {'nome': 'Gabriel Rocha', 'nascimento': datetime(2010, 4, 2), 'idade': 16, 'cpf': '77777777777',
     'uf': 'PE', 'cidade': 'RECIFE', 'posicao': 'LATERAL', 'pe': 'DIREITO', 'altura': 174.0, 'peso': 66.0,
     'clube': 'Sport Sub-17', 'anos_pratica': 6, 'video': '', 'foto': 'foto7.jpg',
     'responsavel': 'Rita Rocha', 'tel_responsavel': '81999990007', 'aceite_termo': 'S',
     'atributos': {'velocidade': 84, 'finalizacao': 45, 'passe': 72, 'drible': 68, 'defesa': 74, 'cabeceio': 60, 'fisico': 78, 'reflexo': 50}, 'score': 75},
    {'nome': 'Lucas Martins', 'nascimento': datetime(2008, 8, 19), 'idade': 18, 'cpf': '88888888888',
     'uf': 'SP', 'cidade': 'SAO PAULO', 'posicao': 'MEIA', 'pe': 'AMBIDESTRO', 'altura': 176.0, 'peso': 69.0,
     'clube': 'Base SP', 'anos_pratica': 8, 'video': 'https://youtu.be/demo8', 'foto': 'foto8.jpg',
     'responsavel': '', 'tel_responsavel': '', 'aceite_termo': '',
     'atributos': {'velocidade': 72, 'finalizacao': 68, 'passe': 86, 'drible': 80, 'defesa': 48, 'cabeceio': 54, 'fisico': 64, 'reflexo': 50}, 'score': 72},
    {'nome': 'Enzo Souza', 'nascimento': datetime(2013, 2, 25), 'idade': 13, 'cpf': '99999999999',
     'uf': 'AM', 'cidade': 'MANAUS', 'posicao': 'ATACANTE', 'pe': 'DIREITO', 'altura': 165.0, 'peso': 58.0,
     'clube': 'Amazonas FC', 'anos_pratica': 4, 'video': '', 'foto': '',
     'responsavel': 'Bruno Souza', 'tel_responsavel': '92999990009', 'aceite_termo': 'S',
     'atributos': {'velocidade': 80, 'finalizacao': 78, 'passe': 58, 'drible': 76, 'defesa': 30, 'cabeceio': 55, 'fisico': 58, 'reflexo': 50}, 'score': 70},
    {'nome': 'Theo Ribeiro', 'nascimento': datetime(2011, 6, 11), 'idade': 15, 'cpf': '10101010101',
     'uf': 'PR', 'cidade': 'CURITIBA', 'posicao': 'ZAGUEIRO', 'pe': 'ESQUERDO', 'altura': 183.0, 'peso': 77.0,
     'clube': 'Base PR', 'anos_pratica': 5, 'video': '', 'foto': 'foto10.jpg',
     'responsavel': 'Sara Ribeiro', 'tel_responsavel': '41999990010', 'aceite_termo': 'S',
     'atributos': {'velocidade': 58, 'finalizacao': 28, 'passe': 62, 'drible': 44, 'defesa': 86, 'cabeceio': 82, 'fisico': 84, 'reflexo': 52}, 'score': 68},
    {'nome': 'Pedro Nunes', 'nascimento': datetime(2009, 10, 3), 'idade': 16, 'cpf': '12121212121',
     'uf': 'RJ', 'cidade': 'DUQUE DE CAXIAS', 'posicao': 'PONTA', 'pe': 'DIREITO', 'altura': 171.0, 'peso': 64.0,
     'clube': 'Base RJ', 'anos_pratica': 6, 'video': '', 'foto': '',
     'responsavel': 'Ivo Nunes', 'tel_responsavel': '21999990011', 'aceite_termo': 'S',
     'atributos': {'velocidade': 86, 'finalizacao': 66, 'passe': 60, 'drible': 84, 'defesa': 26, 'cabeceio': 48, 'fisico': 60, 'reflexo': 50}, 'score': 65},
    {'nome': 'Vitor Barbosa', 'nascimento': datetime(2012, 12, 1), 'idade': 13, 'cpf': '13131313131',
     'uf': 'PE', 'cidade': 'RECIFE', 'posicao': 'VOLANTE', 'pe': 'DIREITO', 'altura': 168.0, 'peso': 60.0,
     'clube': 'Sport Sub-15', 'anos_pratica': 4, 'video': '', 'foto': '',
     'responsavel': 'Lia Barbosa', 'tel_responsavel': '81999990012', 'aceite_termo': 'S',
     'atributos': {'velocidade': 66, 'finalizacao': 50, 'passe': 76, 'drible': 58, 'defesa': 72, 'cabeceio': 62, 'fisico': 74, 'reflexo': 50}, 'score': 62},
]

# peneiras espelhando os eventos da gestora no MVP (presentes/aprovados so nas realizadas)
peneiras = [
    {'codigo': 'E-01', 'cidade': 'Duque de Caxias', 'uf': 'RJ', 'data': '2026-06-15', 'faixa': '13-17',
     'capacidade': 120, 'inscritos': 487, 'status': 'aberta', 'presentes': 102, 'aprovados': 14},
    {'codigo': 'E-02', 'cidade': 'Recife', 'uf': 'PE', 'data': '2026-06-22', 'faixa': '13-17',
     'capacidade': 150, 'inscritos': 612, 'status': 'aberta', 'presentes': 0, 'aprovados': 0},
    {'codigo': 'E-03', 'cidade': 'Manaus', 'uf': 'AM', 'data': '2026-07-05', 'faixa': '13-17',
     'capacidade': 100, 'inscritos': 218, 'status': 'inscricoes', 'presentes': 0, 'aprovados': 0},
    {'codigo': 'E-04', 'cidade': 'São Paulo', 'uf': 'SP', 'data': '2026-05-08', 'faixa': '13-17',
     'capacidade': 180, 'inscritos': 1124, 'status': 'encerrada', 'presentes': 165, 'aprovados': 22},
    {'codigo': 'E-05', 'cidade': 'Curitiba', 'uf': 'PR', 'data': '2026-05-22', 'faixa': '13-17',
     'capacidade': 120, 'inscritos': 543, 'status': 'encerrada', 'presentes': 108, 'aprovados': 16},
]

# perfil-base de cada posicao: dicionario de dicionarios (7 posicoes x 8 atributos)
perfis_posicao = {
    'GOLEIRO':  {'velocidade': 40, 'finalizacao': 20, 'passe': 55, 'drible': 25, 'defesa': 90, 'cabeceio': 50, 'fisico': 70, 'reflexo': 95},
    'ZAGUEIRO': {'velocidade': 55, 'finalizacao': 25, 'passe': 60, 'drible': 40, 'defesa': 90, 'cabeceio': 85, 'fisico': 85, 'reflexo': 50},
    'LATERAL':  {'velocidade': 85, 'finalizacao': 45, 'passe': 72, 'drible': 68, 'defesa': 75, 'cabeceio': 55, 'fisico': 80, 'reflexo': 50},
    'VOLANTE':  {'velocidade': 65, 'finalizacao': 45, 'passe': 80, 'drible': 55, 'defesa': 85, 'cabeceio': 65, 'fisico': 85, 'reflexo': 50},
    'MEIA':     {'velocidade': 70, 'finalizacao': 70, 'passe': 90, 'drible': 85, 'defesa': 45, 'cabeceio': 50, 'fisico': 65, 'reflexo': 50},
    'PONTA':    {'velocidade': 90, 'finalizacao': 72, 'passe': 65, 'drible': 90, 'defesa': 30, 'cabeceio': 50, 'fisico': 65, 'reflexo': 50},
    'ATACANTE': {'velocidade': 85, 'finalizacao': 90, 'passe': 60, 'drible': 80, 'defesa': 30, 'cabeceio': 72, 'fisico': 75, 'reflexo': 55},
}

# matriz de check-in: cada linha = 1 atleta -> [indice_do_atleta, presente] (1 veio / 0 faltou)
presencas = [
    [0, 1], [1, 1], [2, 1], [3, 0], [4, 1], [5, 1],
    [6, 0], [7, 1], [8, 1], [9, 0], [10, 1], [11, 1],
]

# matriz de avaliacao do olheiro: [indice, tecnica, fisico, tatico, atitude] (0 a 10)
avaliacoes = [
    [0, 9, 8, 9, 8],
    [1, 8, 7, 9, 8],
    [2, 7, 9, 8, 7],
    [4, 7, 8, 7, 8],
    [5, 6, 7, 6, 9],
    [7, 7, 6, 8, 7],
]

favoritos = set()  # indices dos atletas favoritados pelo olheiro
decisoes = []      # decisoes do olheiro: cada item = {'indice', 'decisao', 'obs'}

# funil da campanha (numeros agregados do dashboard da gestora, vindos do MVP)
funil_campanha = {'Inscritos': 18420, 'Elegiveis': 16812, 'Convocados': 1850,
                  'Presentes': 1473, 'Aprovados': 187}

# demanda por regiao: lista de dicts (regiao, uf, inscritos, tem peneira ativa, score de demanda)
demanda_regioes = [
    {'regiao': 'SP / Capital', 'uf': 'SP', 'inscritos': 1124, 'peneira_ativa': True, 'demanda': 92},
    {'regiao': 'Recife', 'uf': 'PE', 'inscritos': 612, 'peneira_ativa': True, 'demanda': 95},
    {'regiao': 'Curitiba', 'uf': 'PR', 'inscritos': 543, 'peneira_ativa': True, 'demanda': 81},
    {'regiao': 'Caxias / Baixada', 'uf': 'RJ', 'inscritos': 487, 'peneira_ativa': True, 'demanda': 78},
    {'regiao': 'Salvador', 'uf': 'BA', 'inscritos': 421, 'peneira_ativa': False, 'demanda': 74},
    {'regiao': 'Fortaleza', 'uf': 'CE', 'inscritos': 389, 'peneira_ativa': False, 'demanda': 71},
    {'regiao': 'Belo Horizonte', 'uf': 'MG', 'inscritos': 312, 'peneira_ativa': False, 'demanda': 61},
    {'regiao': 'Manaus', 'uf': 'AM', 'inscritos': 218, 'peneira_ativa': True, 'demanda': 66},
    {'regiao': 'Belem', 'uf': 'PA', 'inscritos': 205, 'peneira_ativa': False, 'demanda': 62},
    {'regiao': 'Teresina', 'uf': 'PI', 'inscritos': 160, 'peneira_ativa': False, 'demanda': 58},
]

# pipeline de talentos (revenue share): lista de dicts com estagio e valor gerado
pipeline_talentos = [
    {'nome': 'Rafael Mendes', 'estagio': 'EM FORMACAO', 'desde': '12/05/2026', 'regiao': 'Sul', 'score': 89, 'valor': 'R$ 0'},
    {'nome': 'Gabriel Lima', 'estagio': 'EM FORMACAO', 'desde': '03/05/2026', 'regiao': 'Sudeste', 'score': 79, 'valor': 'R$ 0'},
    {'nome': 'Diego Ramos', 'estagio': 'CONTRATADO', 'desde': '14/09/2025', 'regiao': 'Nordeste', 'score': 88, 'valor': 'R$ 80k'},
    {'nome': 'Felipe Souza', 'estagio': 'EM FORMACAO', 'desde': '20/04/2026', 'regiao': 'Centro-Oeste', 'score': 81, 'valor': 'R$ 0'},
    {'nome': 'Andre Pinto', 'estagio': 'NEGOCIADO', 'desde': '02/02/2025', 'regiao': 'Sudeste', 'score': 91, 'valor': 'R$ 1,4M'},
]
