"""Painel da gestora (academia): dashboard, mapa de calor, pipeline e peneiras."""

from datetime import datetime
import dados
from dados import moldura

def saudacao():
    """Saudacao conforme a hora do dia.

    retorno (str): 'BOM DIA', 'BOA TARDE' ou 'BOA NOITE'.
    """
    h = datetime.now().hour
    if h < 12:
        return 'BOM DIA'
    if h < 18:
        return 'BOA TARDE'
    return 'BOA NOITE'

def intensidade(demanda):
    """Classifica a demanda de uma regiao (usado no mapa de calor).

    demanda (int): score de demanda 0-100.
    retorno (str): 'CRITICA', 'FORTE' ou 'MEDIA'.
    """
    if demanda > 85:
        return 'CRITICA'
    if demanda >= 65:
        return 'FORTE'
    return 'MEDIA'

def gestora_dashboard():
    """Dashboard da gestao: KPIs, funil de conversao, demanda por regiao e proximas peneiras.

    retorno (None): so imprime os blocos.
    """
    funil = dados.funil_campanha
    inscritos = funil['Inscritos']
    presentes = funil['Presentes']
    aprovados = funil['Aprovados']
    conversao = aprovados / presentes * 100 if presentes else 0  # aprovados / presentes
    cidades = len({d['uf'] for d in dados.demanda_regioes})

    kpis = (f'{saudacao()}, GESTOR(A)\n\n'
            f'Inscritos (campanha) ... {inscritos}  (+412 hoje)\n'
            f'Cidades atingidas ...... {cidades}\n'
            f'Conversao final ........ {conversao:.1f}% (aprovados/presentes)\n'
            f'ROI medio .............. R$ 38 por inscricao valida\n'
            f'Aprovados .............. {aprovados} em formacao')
    moldura(kpis, 'DASHBOARD')

    linhas = []
    anterior = inscritos
    for etapa, qtd in funil.items():
        pct = round(qtd / anterior * 100) if anterior else 0
        barra = '#' * int(qtd / inscritos * 30) if inscritos else ''
        linhas.append(f'{etapa:<11} {qtd:>7}  ({pct:>3}%) {barra}')
        anterior = qtd
    moldura('\n'.join(linhas), 'FUNIL DE CONVERSAO')

    linhas = []
    top = sorted(dados.demanda_regioes, key=lambda d: d['inscritos'], reverse=True)[:5]
    for d in top:
        ativa = 'SIM' if d['peneira_ativa'] else 'NAO'
        sugestao = '-' if d['peneira_ativa'] else 'ABRIR PENEIRA'
        linhas.append(f'{d["regiao"]+" ("+d["uf"]+")":<22} {d["inscritos"]:>5} insc | '
                      f'ativa: {ativa:<3} | demanda {d["demanda"]} | {sugestao}')
    moldura('\n'.join(linhas), 'DEMANDA POR REGIAO (top 5)')

    linhas = []
    for p in dados.peneiras:
        if p['status'] != 'encerrada':
            linhas.append(f'{p["cidade"]:<18} {p["data"]} | {p["inscritos"]} insc | {p["capacidade"]} vagas')
    moldura('\n'.join(linhas), 'PROXIMAS PENEIRAS')

def gestora_mapa():
    """Mapa de calor: demanda por regiao com filtro validado e ranking de reprimidas.

    retorno (None): so imprime os blocos.
    """
    print('Filtro: [T]udo  [D]emanda  [C]obertura  [R]eprimida')
    while True:
        f = input('filtro> ').strip().upper()
        if f in ('T', 'D', 'C', 'R'):
            break
        print('Digite T, D, C ou R.')

    regioes = list(dados.demanda_regioes)
    if f == 'C':                       # cobertura: so quem ja tem peneira ativa
        regioes = [d for d in regioes if d['peneira_ativa']]
    elif f == 'R':                     # demanda reprimida: sem peneira ativa
        regioes = [d for d in regioes if not d['peneira_ativa']]
    regioes.sort(key=lambda d: d['demanda'], reverse=True)

    linhas = []
    for d in regioes:
        barra = '#' * int(d['demanda'] / 5)
        ativa = 'com peneira' if d['peneira_ativa'] else 'SEM peneira'
        linhas.append(f'{d["uf"]}  {d["demanda"]:>3}  {intensidade(d["demanda"]):<7} {barra:<20} {ativa}')
    moldura('\n'.join(linhas), f'MAPA DE CALOR - {len(regioes)} regiao(oes)')

    reprimidas = sorted((d for d in dados.demanda_regioes if not d['peneira_ativa']),
                        key=lambda d: d['demanda'], reverse=True)[:5]
    linhas = [f'{i:02d} {d["regiao"]+" ("+d["uf"]+")":<22} {d["demanda"]}'
              for i, d in enumerate(reprimidas, 1)]
    moldura('\n'.join(linhas), 'TOP DEMANDAS REPRIMIDAS')

def gestora_pipeline():
    """Pipeline de talentos (revenue share): estagios e valor gerado.

    retorno (None): so imprime os blocos.
    """
    moldura('Aprovados ativos ....... 187 em formacao\n'
            'Contratados ............ 24 desde 2025\n'
            'Negociados ............. 3 transferencias\n'
            'Valor gerado ........... R$ 2,1M acumulado', 'PIPELINE DE TALENTOS')

    linhas = ['ATLETA               ESTAGIO       DESDE       REGIAO        SCORE  VALOR']
    for t in dados.pipeline_talentos:
        linhas.append(f'{t["nome"]:<20} {t["estagio"]:<13} {t["desde"]:<11} {t["regiao"]:<13} '
                      f'{t["score"]:>4}   {t["valor"]}')
    moldura('\n'.join(linhas), 'ATLETAS NO PIPELINE')

def gestora_eventos():
    """Operacao das peneiras: cards com status, inscritos, vagas e resultado.

    retorno (None): imprime os cards e um relatorio por codigo (input validado).
    """
    for p in dados.peneiras:
        linhas = [f'[{p["status"].upper()}] {p["codigo"]} - {p["cidade"]}/{p["uf"]}',
                  f'{p["data"]} - faixa {p["faixa"]}',
                  f'Inscritos: {p["inscritos"]} | Vagas: {p["capacidade"]}']
        if p['presentes'] > 0:
            taxa = round(p['aprovados'] / p['presentes'] * 100) if p['presentes'] else 0
            linhas.append(f'Resultado: {p["presentes"]} pres. - {p["aprovados"]} aprov. - {taxa}% taxa')
        moldura('\n'.join(linhas), p['codigo'])

    # relatorio de uma peneira (input validado por codigo)
    codigos = [p['codigo'] for p in dados.peneiras]
    escolha = input('\nCodigo da peneira p/ relatorio (Enter p/ voltar): ').strip().upper()
    if not escolha:
        return
    while escolha not in codigos:
        print(f'Codigo invalido. Use um destes: {", ".join(codigos)}')
        escolha = input('Codigo da peneira (Enter p/ voltar): ').strip().upper()
        if not escolha:
            return
    p = next(pen for pen in dados.peneiras if pen['codigo'] == escolha)
    ocup = round(p['inscritos'] / p['capacidade'] * 100) if p['capacidade'] else 0
    linhas = [f'{p["codigo"]} - {p["cidade"]}/{p["uf"]}',
              f'Status: {p["status"].upper()} | Data: {p["data"]} | Faixa: {p["faixa"]}',
              f'Ocupacao: {p["inscritos"]}/{p["capacidade"]} ({ocup}%)']
    if p['presentes'] > 0:
        taxa = round(p['aprovados'] / p['presentes'] * 100) if p['presentes'] else 0
        linhas.append(f'Comparecimento: {p["presentes"]} presentes | Aprovados: {p["aprovados"]} ({taxa}%)')
    else:
        linhas.append('Ainda sem resultado (peneira nao realizada).')
    moldura('\n'.join(linhas), 'RELATORIO')

def painel_gestora():
    """Nav bar da gestora (academia): dashboard, mapa, pipeline e peneiras.

    retorno (None): roda ate o usuario escolher sair.
    """
    while True:
        print('\n[D] DASHBOARD  [M] MAPA DE CALOR  [P] PIPELINE  [E] PENEIRAS  [S] SAIR')
        op = input('gestora> ').strip().upper()
        if op == 'D':
            gestora_dashboard()
        elif op == 'M':
            gestora_mapa()
        elif op == 'P':
            gestora_pipeline()
        elif op == 'E':
            gestora_eventos()
        elif op == 'S':
            return
        else:
            print('Digite D, M, P, E ou S.')
