"""Area do jogador (atleta): inscricao, feed, tela de status e score de completude."""

import random
import time
from datetime import datetime, date
import textos
import dados
from dados import moldura, console, POSICOES, ESTADOS, IDADE_MIN, IDADE_MAX, PE_DOMINANTE
from olheiro import match_posicao  # reaproveita o calculo de % de match por posicao
from rich.progress import Progress, BarColumn, TextColumn
from rich.panel import Panel

def calcular_score(atleta):
    """Score de completude do perfil (0 a 100, teto 100).

    atleta (dict): dados do atleta.
    retorno (int): soma dos pesos dos campos preenchidos.
    """
    pesos = {'nome': 8, 'nascimento': 8, 'cpf': 10, 'posicao': 10,
             'pe': 4, 'altura': 4, 'peso': 4, 'clube': 6,
             'anos_pratica': 4, 'video': 18, 'foto': 8}
    total = 0
    for campo, ponto in pesos.items():
        if atleta.get(campo):
            total += ponto
    if atleta.get('uf') and atleta.get('cidade'):  # UF + cidade contam juntos
        total += 8
    if atleta.get('aceite_termo') == 'S':          # aceite do responsavel (menor)
        total += 8
    return min(total, 100)

def mostrar_score_rich(score):
    """Mostra o score de completude com a barra da Rich, enchendo ate o valor.

    score (int): valor de 0 a 100.
    retorno (None): so imprime no terminal.
    """
    if score >= 80:
        faixa, cor = 'ALTO', 'green'
    elif score >= 60:
        faixa, cor = 'BOM', 'yellow'
    else:
        faixa, cor = 'INICIAL', 'red'
    with Progress(TextColumn('[bold]COMPLETUDE'), BarColumn(bar_width=40),
                  TextColumn('{task.percentage:>3.0f}%'), console=console) as barra:
        tarefa = barra.add_task('score', total=100)
        for _ in range(score):
            barra.update(tarefa, advance=1)
            time.sleep(0.01)
    console.print(Panel(f'Seu score: [bold {cor}]{score}%[/] - perfil {faixa}', border_style=cor))

def tela_status(nome='ATLETA'):
    """Dashboard pos-login do jogador (tela status do MVP), com dados sorteados.

    nome (str): nome exibido no topo.
    retorno (None): so imprime a convocacao.
    """
    peneira = random.choice(dados.peneiras)
    score = random.randint(70, 99)
    ranking = random.randint(1, peneira['inscritos'])
    vaga = random.randint(1, peneira['capacidade'])
    bloco = (
        f'OLA, {nome.upper()}                         [CONVOCADO]\n'
        f'VOCE FOI CONVOCADO.\n\n'
        f'SUA PROXIMA PENEIRA: {peneira["cidade"].upper()} - {peneira["uf"]}\n'
        f'DATA: {peneira["data"]}\n'
        f'SUA VAGA: #{vaga:03d}/{peneira["capacidade"]}\n'
        f'SEU SCORE: {score}%   RANKING: #{ranking} entre {peneira["inscritos"]}\n\n'
        f'LINHA DO TEMPO\n'
        f'  [x] Inscricao realizada\n'
        f'  [x] Score consolidado em {score}%\n'
        f'  [x] Convocacao confirmada via SMS\n'
        f'  [ ] Peneira presencial - {peneira["cidade"]}\n'
        f'  [ ] Avaliacao do olheiro\n'
        f'  [ ] Resposta final\n\n'
        f'LEMBRETE: chegue com 30 min de antecedencia, leve documento\n'
        f'com foto e a confirmacao por SMS.'
    )
    moldura(bloco, 'STATUS DO ATLETA')

def inscricao():
    """Wizard de inscricao do atleta em 5 passos (identificacao a responsavel).

    retorno (None): salva o atleta em dados.atletas e mostra o score.
    """
    print('QUEM E VOCE?')
    nome_completo = input('Seu Nome Completo: ')

    while True:
        try:
            data_de_nascimento = input('DD/MM/YYYY: ')
            data_de_nascimento = datetime.strptime(data_de_nascimento, "%d/%m/%Y")
            hoje = date.today()
            idade = hoje.year - data_de_nascimento.year
            if (hoje.month, hoje.day) < (data_de_nascimento.month, data_de_nascimento.day):
                idade -= 1  # ainda nao fez aniversario este ano
            if idade < IDADE_MIN or idade > IDADE_MAX:
                print(f'Idade fora da faixa permitida (07-19). Voce tem {idade}.')
            else:
                break
        except ValueError:
            print('Data invalida! Digite novamente.')

    while True:
        cpf = input('CPF - 11 digitos - SOMENTE NUMEROS: ').strip()
        if cpf.isdigit() and len(cpf) == 11:
            break
        print('Digite um CPF valido (11 numeros)!')

    # cada campo tem seu proprio loop: repete so a pergunta que veio errada
    while True:
        estado = input('ESTADO (UF, ex: RJ): ').strip().upper()
        if estado in ESTADOS:
            break
        print('Informe uma UF valida (ex: RJ).')

    while True:
        cidade = input('SUA CIDADE: ').strip().upper()
        if cidade:
            break
        print('Informe a cidade onde voce mora.')

    print('COMO VOCE JOGA?')

    while True:
        posicao = input(f'Selecione uma posicao {POSICOES}: ').strip().upper()
        if posicao in POSICOES:
            break
        print('Digite uma posicao da lista!')

    while True:
        pe_dominante = input('PE DOMINANTE (DIREITO/ESQUERDO/AMBIDESTRO): ').strip().upper()
        if pe_dominante in PE_DOMINANTE:
            break
        print('Digite: DIREITO, ESQUERDO ou AMBIDESTRO.')

    while True:
        try:
            altura = float(input('ALTURA (CM): ').replace(',', '.'))
            if altura <= 0:
                print('A altura tem que ser maior que zero.')
                continue
            break
        except ValueError:
            print('Digite a altura em numero (ex: 178).')

    while True:
        try:
            peso = float(input('PESO (KG): ').replace(',', '.'))
            if peso <= 0:
                print('O peso tem que ser maior que zero.')
                continue
            break
        except ValueError:
            print('Digite o peso em numero (ex: 70).')

    while True:
        onde_joga = input('NOME DA ESCOLA OU CLUBE AONDE VOCE JOGA: ').strip()
        if onde_joga:
            break
        print('Informe onde voce joga.')

    while True:
        try:
            tempo_de_pratica = int(input('TEMPO DE PRATICA (ANOS): '))
            if tempo_de_pratica < 0:
                print('Nao pode ser negativo.')
                continue
            break
        except ValueError:
            print('Digite um numero inteiro de anos (ex: 5).')

    print('MIDIAS (opcional - de Enter para pular)')
    video = input('Link do seu video (YouTube/Instagram): ').strip()
    foto = input('Caminho ou link da sua foto: ').strip()

    # PASSO 5 - responsavel (condicional: so menor de 18)
    if idade >= 18:
        print('VOCE E MAIOR. SEM NECESSIDADE DE RESPONSAVEL.')
        nome_responsavel = ''
        telefone_responsavel = ''
        aceite = ''
    else:
        nome_responsavel = input('Nome Completo do Responsavel: ').strip()
        while not nome_responsavel:
            print('Informe o nome completo do responsavel legal.')
            nome_responsavel = input('Nome Completo do Responsavel: ').strip()

        telefone_responsavel = input('CELULAR DO RESPONSAVEL (so numeros, com DDD): ').strip()
        while not telefone_responsavel.isdigit():
            print('Digite o celular com DDD, apenas numeros.')
            telefone_responsavel = input('CELULAR DO RESPONSAVEL (so numeros, com DDD): ').strip()

        aceite = input('ACEITO O TERMO RESPONSAVEL? [S/N] ').strip().upper()
        while aceite not in ('S', 'N'):
            print('Digite apenas S ou N!')
            aceite = input('ACEITO O TERMO RESPONSAVEL? [S/N] ').strip().upper()

        if aceite == 'N':
            print('Sem o aceite do responsavel nao e possivel concluir a inscricao.')
            return

    atleta = {
        'nome': nome_completo,
        'nascimento': data_de_nascimento,  # datetime -> formatar com strftime ao exibir
        'idade': idade,
        'cpf': cpf,
        'uf': estado,
        'cidade': cidade,
        'posicao': posicao,
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
        'atributos': {},  # 8 atributos tecnicos: preenchidos depois (tela perfil)
        'score': 0,       # score de completude: calculado abaixo
    }
    atleta['score'] = calcular_score(atleta)
    dados.atletas.append(atleta)

    input('APERTE ENTER PARA CONFIRMAR A INSCRICAO! ')
    moldura('Inscricao enviada. Perfil criado. Voce esta no jogo.\n'
            'Voce recebe SMS com a confirmacao e sera alocado na peneira\n'
            'mais proxima com vaga.', 'INSCRICAO')
    mostrar_score_rich(atleta['score'])  # barra de completude com a Rich

def feed():
    """Feed de atletas com filtro por posicao e por estado.

    retorno (None): so imprime a lista filtrada.
    """
    print(textos.FEED)
    print('Posicoes:', ', '.join(sorted(POSICOES)))

    posicao_feed = input('POSICAO (Enter para todas): ').strip().upper()
    while posicao_feed and posicao_feed not in POSICOES:
        print('Posicao invalida! Escolha uma da lista ou de Enter para todas.')
        posicao_feed = input('POSICAO (Enter para todas): ').strip().upper()

    estado_feed = input('ESTADO (Enter para todos): ').strip().upper()
    while estado_feed and estado_feed not in ESTADOS:
        print('Estado invalido! Use a sigla (ex: RJ) ou de Enter para todos.')
        estado_feed = input('ESTADO (Enter para todos): ').strip().upper()

    filtrados = []
    for a in dados.atletas:
        if posicao_feed and a['posicao'] != posicao_feed:
            continue
        if estado_feed and a['uf'] != estado_feed:
            continue
        filtrados.append(a)

    if not filtrados:
        print('Nenhum atleta com esses filtros. Tente outra posicao ou outro estado.')
        return

    linhas = []
    for a in filtrados:
        linhas.append(f"{a['nome']} | {a['posicao']} | {a['cidade']}/{a['uf']} | "
                      f"{a['idade']} anos | score {a['score']}")
    moldura('\n'.join(linhas), f'FEED - {len(filtrados)} atleta(s)')

def perfil():
    """Perfil tatico do atleta: biometria, 8 atributos, % de match, midias e plano.

    retorno (None): mostra a ficha do atleta escolhido (espelha a tela perfil do MVP).
    """
    linhas = [f'  #{i:03d} {a["nome"]:<20} {a["posicao"]}' for i, a in enumerate(dados.atletas)]
    moldura('\n'.join(linhas), 'PERFIL - ESCOLHA O ATLETA')

    escolha = input('\n# do atleta (Enter p/ voltar): ').strip()
    if not escolha:
        return
    if not escolha.isdigit() or int(escolha) >= len(dados.atletas):
        print('# invalido.')
        return
    a = dados.atletas[int(escolha)]

    linhas = [f'{a["nome"]} - {a["posicao"]} - {a["idade"]} anos - {a["cidade"]}/{a["uf"]}',
              f'Altura: {a["altura"]}cm | Peso: {a["peso"]}kg | Pe: {a["pe"]} | '
              f'Pratica: {a["anos_pratica"]} anos',
              f'Score de completude: {a["score"]}']
    if a['atributos']:
        linhas.append('')
        linhas.append('ATRIBUTOS')
        for k, v in a['atributos'].items():
            linhas.append(f'  {k.capitalize():<12} {v}')
        matches = sorted(((match_posicao(a['atributos'], p), pos)
                          for pos, p in dados.perfis_posicao.items()), reverse=True)
        linhas.append('PERFIL TATICO SUGERIDO (similaridade de cosseno)')
        for pct, pos in matches[:4]:
            linhas.append(f'  {pos:<10} {pct:.0f}% match')
    linhas.append('')
    linhas.append(f'MIDIAS: video {"sim" if a["video"] else "nao"} | foto {"sim" if a["foto"] else "nao"}')
    linhas.append('PLANO: Gratuito (ve faixas) | Premium R$ 14,90 (score detalhado + ranking)')
    moldura('\n'.join(linhas), 'PERFIL DO ATLETA')
