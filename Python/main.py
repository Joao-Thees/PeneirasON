import msvcrt
'''atletas = {[]}
peneiras = {[]}
perfis_posicao = {{}}
presencas = [[]]
avaliacoes = [[]]'''

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
        print('''
                Como funciona
                Três passos.
                Um campo aberto.

                Sem boca a boca. Sem conexão. Sem precisar conhecer quem está no clube. O sistema organiza tudo: inscrição, alocação geográfica e ranking pelo olheiro.
                01
                Inscreva-se

                Formulário em 4 minutos. Pré-validação automática de idade (07–19) e termo de responsável.
                Score 0 → 100% em tempo real.
                02
                Seja convocado

                O algoritmo aloca os inscritos na peneira mais próxima com vaga, priorizando regiões historicamente esquecidas.
                Notificação por SMS + e-mail.
                03
                Mostre seu futebol

                O olheiro chega ao campo com sua lista. Você joga. Avaliação por critério: técnica, físico, tático, atitude.
                Pipeline rastreável para sempre.
                ''')
def sobre():
    print('''
            Quem somos
            Quem está
            por trás
            do projeto.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Mauris sit amet velit non lectus dignissim suscipit.
            Fundado em
            2026
            FIAP · 1º Ano
            Equipe
            5
            engenheiros
            Estados atingidos
            14
            meta 2027: 27
            Inscritos · campanha
            18.4k
            +412 hoje
            Direção
            Missão.
            Visão.
            Valores.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent in sapien sed leo vestibulum convallis. Integer non lectus eu lorem fringilla volutpat.
            01
            Missão
            Democratizar o futebol.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore.
            02
            Visão
            O olheiro vai até você.

            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            03
            Valores
            Acesso, dado, respeito.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore.
            Histórico
            Do briefing
            ao campo.

            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore. Vestibulum ante ipsum primis in faucibus orci luctus.
            FEV · 2026
            Kickoff com a Pelé Academia

            Briefing inicial. Mapeamento do problema: peneiras manuais, alcance restrito, falta de inteligência operacional.
            MAR · 2026
            Pesquisa de campo

            Entrevistas com olheiros, gestores e potenciais inscritos em três regiões: RJ, PE e AM. Lorem ipsum dolor sit amet.
            ABR · 2026
            Design system + protótipo

            Sistema de design publicado. Primeiros protótipos navegáveis testados com usuários reais.
            MAI · 2026
            Sprint 1 — MVP

            Inscrição, score de completude, alocação geográfica e painel do olheiro entregues.
            JUN · 2026
            Primeira peneira piloto

            Caxias/RJ. 487 inscritos, 120 vagas, 102 presentes, 14 aprovados.
            Q3 · 2026
            Expansão Nordeste

            Peneiras em Recife, Salvador e Fortaleza. Integração de SMS multi-operadora.
            2027
            Cobertura nacional

            Meta de 27 estados, modelo de revenue share ativo, ML preditivo em produção.
            Equipe
            Cinco pessoas.
            Uma plataforma.
            foto
            Arthur Alen Amorelli Pereira
            Tech LeadRM 571897
            foto
            João Thees Castro Santiago
            BackendRM 572829
            foto
            Caio Viana de Faria
            FrontendRM 570634
            foto
            Clara Diel Gama Secco
            Design + DPORM 571679
            foto
            Anna
            ProdutoRM —
            Parceria
            Em parceria com a
            Pelé Academia.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fundada em 2018 para honrar o legado do Rei Pelé, a Pelé Academia oferece a crianças e jovens brasileiros acesso à educação, lazer e cidadania através do futebol.

            Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
            Em números
            Anos de operação8
            Atletas atendidos12k+
            Núcleos no Brasil24
            Escolas parceiras146
            Contato
            Fala
            com a gente.

            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
            E-mail geral contato@exemplo.com
            Imprensa imprensa@exemplo.com
            Parcerias parcerias@exemplo.com
            Encarregado (DPO) dpo@exemplo.com
            Telefone (00) 0000-0000
            Endereço Rua Exemplo, 000 — Cidade/UF — 00000-000 ''')

    print('VOLTAR A HOME - QUERO ME INSCREVER [PRESSIONE CNTRL + H PARA HOME OU CNTRL + I PARA INSCRIÇÃO]: ')
    tecla = msvcrt.getch()
    if tecla == b'\t': 
        return header()
    elif tecla == b'\x08':
        pass # por enquanto pass pois ainda nao criei a funcao de inscricao
    else:
        try:
            print('PRESSIONE APENAS CNTR + I OU CNTRL + H!')
        except:
            header()



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
    pass
rotas_header = {"como funciona": como_funciona,
                "sobre": sobre,
                "faq": faq,
                "politica de privacidade": politica_de_priv
                }

if rota in rotas_header:
    rotas_header[rota]()
else:
    print('Error 404')

