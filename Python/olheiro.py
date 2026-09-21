"""Painel do olheiro: lista de inscritos, check-in e avaliacao no campo."""

import dados
from dados import moldura, POSICOES, ESTADOS, IDADE_MIN, IDADE_MAX

def media_avaliacao(linha):
    """Media simples dos 4 criterios de uma avaliacao.

    linha (list): [indice, tecnica, fisico, tatico, atitude].
    retorno (float): media dos 4 criterios.
    """
    return sum(linha[1:5]) / 4

def match_posicao(atributos, perfil):
    """Similaridade de cosseno (%) entre os atributos do atleta e um perfil-base.

    atributos (dict): 8 atributos do atleta.
    perfil (dict): 8 atributos do perfil-base da posicao.
    retorno (float): porcentagem de match (0 a 100).
    """
    a = [atributos[k] for k in perfil]
    b = [perfil[k] for k in perfil]
    dot = sum(x * y for x, y in zip(a, b))
    na = sum(x * x for x in a) ** 0.5
    nb = sum(y * y for y in b) ** 0.5
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb) * 100

def kpis_lista():
    """Monta o texto das estatisticas do topo da lista de inscritos.

    retorno (str): bloco com inscritos, elegiveis, convocados, score medio e % com video.
    """
    total = len(dados.atletas)
    if total == 0:
        return 'Nenhum inscrito ainda.'
    # regras que o MVP mostra pronto mas nao explica (implementadas aqui):
    # elegivel = idade na faixa 7-19 e score >= 60; convocado = score >= 85
    elegiveis = sum(1 for a in dados.atletas if IDADE_MIN <= a['idade'] <= IDADE_MAX and a['score'] >= 60)
    convocados = sum(1 for a in dados.atletas if a['score'] >= 85)
    score_medio = round(sum(a['score'] for a in dados.atletas) / total)
    com_video = round(sum(1 for a in dados.atletas if a['video']) / total * 100)
    pct_eleg = round(elegiveis / total * 100, 1)
    return (f'INSCRITOS {total} | ELEGIVEIS {elegiveis} ({pct_eleg}%) | CONVOCADOS {convocados}\n'
            f'SCORE MEDIO {score_medio} | COM VIDEO {com_video}%')

def tela_detalhe_atleta(indice):
    """Ficha completa do inscrito: dados salvos, perfil tatico, historico e notas.

    indice (int): posicao do atleta em dados.atletas.
    retorno (None): so imprime a ficha.
    """
    a = dados.atletas[indice]
    linhas = []
    marca_fav = '(favorito)' if indice in dados.favoritos else ''
    linhas.append(f'#{indice:03d}  {a["nome"]}  {marca_fav}')
    linhas.append(f'{a["posicao"]} - {a["idade"]} anos - {a["cidade"]}/{a["uf"]}')
    linhas.append('DADOS DO CADASTRO (retomados sem perder nada)')
    linhas.append(f'  Pe: {a["pe"]} | Altura: {a["altura"]}cm | Peso: {a["peso"]}kg')
    linhas.append(f'  Clube: {a["clube"]} | Tempo de pratica: {a["anos_pratica"]} anos')
    linhas.append(f'  Video: {a["video"] or "sem video"} | Foto: {a["foto"] or "sem foto"}')
    linhas.append(f'  Score de completude: {a["score"]}')
    if a['atributos']:
        linhas.append('PERFIL TATICO (atributos)')
        for k, v in a['atributos'].items():
            linhas.append(f'  {k.capitalize():<12} {v}')
        matches = sorted(
            ((match_posicao(a['atributos'], p), pos) for pos, p in dados.perfis_posicao.items()),
            reverse=True)
        linhas.append('PERFIL TATICO SUGERIDO (similaridade de cosseno):')
        for pct, pos in matches[:3]:
            linhas.append(f'  {pos:<10} {pct:.0f}% match')
    # historico: presenca no check-in
    linha_pres = next((p for p in dados.presencas if p[0] == indice), None)
    linhas.append('HISTORICO')
    if linha_pres is not None:
        linhas.append(f'  Check-in: {"presente" if linha_pres[1] == 1 else "aguardando/faltou"}')
    else:
        linhas.append('  Check-in: sem registro')
    # notas do olheiro
    linha_av = next((av for av in dados.avaliacoes if av[0] == indice), None)
    if linha_av is not None:
        linhas.append(f'  Notas: TEC {linha_av[1]} FIS {linha_av[2]} TAT {linha_av[3]} ATI {linha_av[4]}'
                      f' | media {media_avaliacao(linha_av):.1f}')
    dec = next((d for d in dados.decisoes if d['indice'] == indice), None)
    if dec:
        linhas.append(f'  Decisao: {dec["decisao"]} | obs: {dec["obs"] or "-"}')
    moldura('\n'.join(linhas), 'FICHA DO ATLETA')

def tela_lista():
    """Lista de inscritos: KPIs, filtros, ordenacao e detalhe ao selecionar o #.

    retorno (None): imprime a lista e trata a selecao.
    """
    moldura(kpis_lista(), 'LISTA DE INSCRITOS')

    pos = input('Filtrar posicao (Enter=todas): ').strip().upper()
    while pos and pos not in POSICOES:
        print('Posicao invalida.')
        pos = input('Filtrar posicao (Enter=todas): ').strip().upper()

    uf = input('Filtrar regiao/UF (Enter=todas): ').strip().upper()
    while uf and uf not in ESTADOS:
        print('UF invalida.')
        uf = input('Filtrar regiao/UF (Enter=todas): ').strip().upper()

    so_video = input('So com video? [s/N]: ').strip().lower() == 's'
    so_fav = input('So favoritos? [s/N]: ').strip().lower() == 's'
    ordena = input('Ordenar por [s]core / [i]dade (Enter=score): ').strip().lower()

    # guarda o indice original pra poder favoritar/detalhar depois
    selec = []
    for i, a in enumerate(dados.atletas):
        if pos and a['posicao'] != pos:
            continue
        if uf and a['uf'] != uf:
            continue
        if so_video and not a['video']:
            continue
        if so_fav and i not in dados.favoritos:
            continue
        selec.append(i)

    if ordena == 'i':
        selec.sort(key=lambda i: dados.atletas[i]['idade'])
    else:
        selec.sort(key=lambda i: dados.atletas[i]['score'], reverse=True)

    if not selec:
        print('Nenhum inscrito com esses filtros.')
        return

    linhas = ['   #  ATLETA               POSICAO    IDADE ORIGEM              SCORE VIDEO STATUS']
    for i in selec:
        a = dados.atletas[i]
        estrela = '*' if i in dados.favoritos else ' '
        status = 'CONVOCADO' if a['score'] >= 85 else 'INSCRITO'
        video = '1' if a['video'] else '-'
        origem = f'{a["cidade"]}/{a["uf"]}'
        linhas.append(f'{estrela}{i:>3}  {a["nome"]:<20} {a["posicao"]:<10} {a["idade"]:>4}  '
                      f'{origem:<18} {a["score"]:>4}  {video:>3}   {status}')
    moldura('\n'.join(linhas), f'{len(selec)} resultado(s)')

    # "clicar" no inscrito = digitar o # dele
    while True:
        escolha = input('\n# do atleta p/ detalhe, "f N" p/ (des)favoritar, Enter p/ voltar: ').strip().lower()
        if not escolha:
            return
        if escolha.startswith('f'):
            partes = escolha.split()
            if len(partes) == 2 and partes[1].isdigit() and 0 <= int(partes[1]) < len(dados.atletas):
                idx = int(partes[1])
                if idx in dados.favoritos:
                    dados.favoritos.discard(idx)
                    print(f'{dados.atletas[idx]["nome"]} saiu dos favoritos.')
                else:
                    dados.favoritos.add(idx)
                    print(f'{dados.atletas[idx]["nome"]} marcado como favorito.')
            else:
                print('Use: f seguido do # (ex: f 3).')
            continue
        if escolha.isdigit() and 0 <= int(escolha) < len(dados.atletas):
            tela_detalhe_atleta(int(escolha))
        else:
            print('Digite um # valido.')

def tela_checkin():
    """Check-in do dia: marca presenca por atleta e mostra a % de comparecimento.

    retorno (None): atualiza a matriz dados.presencas.
    """
    busca = input('Buscar atleta por nome (Enter=todos): ').strip().lower()
    while True:
        presentes = sum(1 for p in dados.presencas if p[1] == 1)
        total = len(dados.presencas)
        pct = round(presentes / total * 100) if total else 0
        linhas = [f'COMPARECIMENTO: {presentes} de {total} presentes ({pct}%)']
        for p in dados.presencas:
            idx = p[0]
            if idx >= len(dados.atletas):
                continue
            a = dados.atletas[idx]
            if busca and busca not in a['nome'].lower():
                continue
            marca = '[x]' if p[1] == 1 else '[ ]'
            linhas.append(f'  {marca} #{idx:03d} {a["nome"]:<20} {a["posicao"]:<10} {a["cidade"]}/{a["uf"]}')
        moldura('\n'.join(linhas), 'CHECK-IN DA PENEIRA')
        escolha = input('\n# p/ marcar/desmarcar presenca, Enter p/ voltar: ').strip()
        if not escolha:
            return
        if escolha.isdigit():
            idx = int(escolha)
            for p in dados.presencas:
                if p[0] == idx:
                    p[1] = 0 if p[1] == 1 else 1
                    break
            else:
                print('Esse # nao esta na lista de check-in.')
        else:
            print('Digite um # valido.')

def tela_avaliacao():
    """Avaliacao no campo: 4 criterios 0-10, media, observacao e decisao.

    retorno (None): salva as notas em dados.avaliacoes e a decisao em dados.decisoes.
    """
    linhas = [f'  #{i:03d} {a["nome"]:<20} {a["posicao"]}' for i, a in enumerate(dados.atletas)]
    moldura('\n'.join(linhas), 'AVALIACAO - ESCOLHA O ATLETA')

    escolha = input('\n# do atleta p/ avaliar (Enter p/ voltar): ').strip()
    if not escolha:
        return
    if not escolha.isdigit() or int(escolha) >= len(dados.atletas):
        print('# invalido.')
        return
    idx = int(escolha)
    a = dados.atletas[idx]
    print(f'\nAvaliando: {a["nome"]} - {a["posicao"]} - {a["idade"]} anos - {a["cidade"]}/{a["uf"]}')

    criterios = ('TECNICA', 'FISICO', 'TATICO', 'ATITUDE')
    notas = []
    for c in criterios:
        while True:
            try:
                n = int(input(f'{c} (0-10): '))
                if 0 <= n <= 10:
                    notas.append(n)
                    break
                print('A nota tem que ser de 0 a 10.')
            except ValueError:
                print('Digite um numero inteiro de 0 a 10.')
    media = sum(notas) / 4

    obs = input('OBSERVACOES: ').strip()

    while True:
        d = input('DECISAO - [A]provar / [O]bservar / [D]escartar: ').strip().upper()
        if d in ('A', 'O', 'D'):
            break
        print('Digite A, O ou D.')
    decisao = {'A': 'APROVADO', 'O': 'OBSERVAR', 'D': 'DESCARTADO'}[d]

    # salva as notas na matriz avaliacoes (atualiza se ja existir; senao acrescenta)
    linha = [idx] + notas
    for k, av in enumerate(dados.avaliacoes):
        if av[0] == idx:
            dados.avaliacoes[k] = linha
            break
    else:
        dados.avaliacoes.append(linha)

    # salva a decisao na lista decisoes (atualiza se ja existir)
    for drec in dados.decisoes:
        if drec['indice'] == idx:
            drec['decisao'] = decisao
            drec['obs'] = obs
            break
    else:
        dados.decisoes.append({'indice': idx, 'decisao': decisao, 'obs': obs})

    moldura(f'{a["nome"]}\nMedia: {media:.1f} (TEC {notas[0]} FIS {notas[1]} TAT {notas[2]} ATI {notas[3]})\n'
            f'Decisao: {decisao}\nObs: {obs or "-"}', 'AVALIACAO SALVA')

def painel_olheiro():
    """Nav bar do olheiro: alterna entre lista, check-in e avaliacao.

    retorno (None): roda ate o usuario escolher sair.
    """
    while True:
        print('\n[L] LISTA DE INSCRITOS  [C] CHECK-IN  [A] AVALIACAO  [S] SAIR')
        op = input('olheiro> ').strip().upper()
        if op == 'L':
            tela_lista()
        elif op == 'C':
            tela_checkin()
        elif op == 'A':
            tela_avaliacao()
        elif op == 'S':
            return
        else:
            print('Digite L, C, A ou S.')
