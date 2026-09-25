# usando conceito aprendido recentemente em sala de aula
# constantes -> Toda constante, isto é, uma variavel que não muda, deve ser chamada em maiúscula. Uma convesão do Python.

SOBRE = '''Quem somos
            Quem está
            por trás
            do projeto.
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
            01
            Missão
            Democratizar o futebol.
            02
            Visão
            O olheiro vai até você.
            03
            Valores
            Acesso, dado, respeito.
            Histórico
            Do briefing
            ao campo.
            FEV · 2026
            Kickoff com a Pelé Academia

            Briefing inicial. Mapeamento do problema: peneiras manuais, alcance restrito, falta de inteligência operacional.
            MAR · 2026
            Pesquisa de campo

            Entrevistas com olheiros, gestores e potenciais inscritos em três regiões: RJ, PE e AM.
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
            Anna Júlia Elias Andrade
            ProdutoRM 573453
            Parceria
            Em parceria com a
            Pelé Academia.

            Fundada em 2018 para honrar o legado do Rei Pelé, a Pelé Academia oferece a crianças e jovens brasileiros acesso à educação, lazer e cidadania através do futebol.
            Em números
            Anos de operação8
            Atletas atendidos12k+
            Núcleos no Brasil24
            Escolas parceiras146
            Contato
            Fala
            com a gente.
            E-mail geral contato@exemplo.com
            Imprensa imprensa@exemplo.com
            Parcerias parcerias@exemplo.com
            Encarregado (DPO) dpo@exemplo.com
            Telefone (00) 0000-0000
            Endereço Rua Exemplo, 000 — Cidade/UF — 00000-000'''

COMO_FUNCIONA = '''Como funciona
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
                Pipeline rastreável para sempre.'''

POLITICA_DE_PRIV = '''01
Princípios que guiam esta política
O Peneiras On nasceu para democratizar o acesso ao futebol. Por isso, tratamos dados com três compromissos:

▸
Mínimo necessário. Não pedimos nada além do que precisamos para inscrever, alocar e avaliar o atleta.
▸
Transparência radical. Você sabe o que coletamos, por quê, e pode ver tudo na sua conta.
▸
Proteção redobrada para menores. Como atendemos jovens de 07 a 19 anos, seguimos o ECA além da LGPD.
02
Quais dados coletamos
Coletamos somente o que é necessário para os fluxos da plataforma. Os dados são classificados em três categorias:

Categoria
Conteúdo
Justificativa
Obrigatórios
Nome completo, data de nascimento, CPF, cidade/estado, posição, contato do responsável legal (para menores).
Validar elegibilidade, prevenir fraude e duplicidade, comunicar convocação.
Opcionais
Altura, peso, pé dominante, clube atual, tempo de prática, links de vídeo, foto.
Aumentar o score de completude e dar mais informação ao olheiro.
Gerados
Score, ranking, perfil tático sugerido (radar), histórico de peneiras, avaliações, check-in.
Permitir o trabalho do olheiro e a inteligência operacional da gestão.
Não coletamos dados sensíveis (raça, religião, opinião política, biometria, saúde) — eles não são necessários para o serviço.

03
Para que usamos seus dados
▸
Inscrição e elegibilidade: validar idade (07–19), CPF único, residência.
▸
Alocação geográfica: calcular a peneira mais próxima com vaga (PostGIS).
▸
Comunicação: SMS/e-mail de confirmação, convocação, lembrete e resultado.
▸
Avaliação no campo: registrar notas e parecer do olheiro pós-peneira.
▸
Pipeline de talentos: manter histórico de aprovados para sustentar o revenue share (mecanismo de solidariedade FIFA).
▸
Inteligência estratégica: agregados anônimos por região (mapa de calor, funil) — sem identificar pessoas.
Nunca usamos os dados para perfilamento comercial, publicidade direcionada ou venda a terceiros.
04
Base legal (Art. 7º da LGPD)
Cada tratamento tem uma base legal específica:

Categoria
Conteúdo
Justificativa
Consentimento
Termo aceito pelo responsável (menores) ou pelo próprio inscrito (≥18).
Art. 7º, I
Execução de contrato
Tratamentos indispensáveis para inscrever, convocar e avaliar.
Art. 7º, V
Legítimo interesse
Prevenção de fraude (CPF duplicado) e segurança da plataforma.
Art. 7º, IX
Obrigação legal
Atender ECA, Marco Civil da Internet e ordens judiciais.
Art. 7º, II
05
Menores de idade — proteção reforçada (ECA + LGPD Art. 14)
Atendemos atletas de 07 a 19 anos. Para qualquer pessoa menor de 18, aplicamos camada extra de proteção:

▸
Termo do responsável legal obrigatório na inscrição, guardado com data/hora e IP.
▸
Notificações em duplicidade: SMS de confirmação vai para o celular do responsável.
▸
Acesso parental: o responsável pode excluir a conta do menor a qualquer momento.
▸
Sem dados sensíveis: não coletamos imagens íntimas, saúde ou geolocalização em tempo real.
▸
Sem comunicação direta entre olheiro e menor fora dos canais oficiais.
Suspeita de violação de direitos da criança/adolescente é encaminhada ao Conselho Tutelar e ao Ministério Público, conforme Art. 13 do ECA.
06
Com quem compartilhamos
Categoria
Conteúdo
Justificativa
Olheiros
Perfil completo do inscrito convocado para a peneira em que atuam.
Execução do contrato.
Pelé Academia
Dados agregados e anonimizados; perfis individuais só para gestão.
Co-controlador (parceria).
Operadores
Hospedagem (cloud), SMS, e-mail e analytics — sob contrato de proteção de dados.
Funcionamento técnico.
Autoridades
Quando obrigado por lei, ordem judicial ou requisição do MP / Conselho Tutelar.
Obrigação legal.
Nunca compartilhamos com fins comerciais, parceiros publicitários ou venda de leads.

07
Por quanto tempo guardamos
Categoria
Conteúdo
Justificativa
Cadastro ativo
Enquanto a conta estiver em uso.
Manter histórico de peneiras.
Cadastro inativo
24 meses após o último login.
Depois, conta é anonimizada.
Pipeline aprovados
Até a maioridade + 10 anos, ou prazo do revenue share.
Documentar formação (FIFA).
Logs de segurança
6 meses.
Marco Civil (Art. 15).
Você pode pedir a exclusão antecipada a qualquer momento — atendemos em até 15 dias.

08
Seus direitos como titular (Art. 18 da LGPD)
Você (ou o responsável legal, se for menor) pode exercer estes direitos a qualquer momento:

I
Confirmação
Saber se tratamos seus dados.
II
Acesso
Receber uma cópia de tudo que temos.
III
Correção
Pedir ajuste de dados incompletos ou desatualizados.
IV
Anonimização
Bloquear ou anonimizar dados desnecessários.
V
Portabilidade
Levar seus dados em formato estruturado para outro serviço.
VI
Exclusão
Apagar tudo (exceto o que devemos guardar por lei).
VII
Compartilhamento
Saber com quem compartilhamos.
VIII
Revogação
Cancelar o consentimento dado anteriormente.
IX
Revisão humana
Pedir revisão de decisões automatizadas (ex.: score, ranking).
Como exercer? Em qualquer um destes canais:

▸
Pelo painel Configurações → Privacidade dentro da plataforma.
▸
Por e-mail ao Encarregado: dpo@exemplo.com.
▸
Pelo formulário público em exemplo.com/direitos.
Prazo de resposta: até 15 dias, conforme Art. 19 da LGPD.

09
Como protegemos os dados
Categoria
Conteúdo
Justificativa
Em repouso
Banco de dados criptografado com AES-256.
Dados ilegíveis mesmo se vazarem.
Em trânsito
TLS 1.3 em todas as conexões.
Impede interceptação na rede.
Senhas
Hash bcrypt com fator de custo ≥ 12.
Impossível reverter à senha original.
Acesso interno
RBAC + auditoria de acesso por usuário/IP.
Quem viu o quê fica registrado.
Backup
Snapshot a cada 6h, retenção 30 dias.
RPO 6h, RTO 2h.
Em caso de incidente com risco aos titulares, comunicamos a ANPD e os afetados em até 72 horas (Art. 48 da LGPD).
10
Cookies e tecnologias similares
Usamos três tipos de cookies. Você pode gerenciar tudo em Configurações → Cookies.

Categoria
Conteúdo
Justificativa
Essenciais
Sessão de login, prevenção de CSRF, preferência de idioma.
Indispensáveis.
Funcionais
Lembrar filtros do olheiro, último estado do dashboard.
Opcionais.
Analytics
Métricas agregadas anônimas (volume, tempo na página).
Opcionais. Sem identificação.
Não usamos cookies de publicidade ou de redes sociais.

11
Encarregado de Proteção de Dados (DPO)
O Encarregado recebe suas solicitações, reclamações e comunica a ANPD em caso de incidente.

Nome
Nome do Encarregado
Cargo
DPO — Peneiras On
E-mail
dpo@exemplo.com
Telefone
(00) 0000-0000
Endereço
Rua Exemplo, 000 — Cidade/UF — 00000-000
Horário
Seg–Sex · 09h às 18h (BRT)
Você também pode reclamar diretamente à Autoridade Nacional de Proteção de Dados (ANPD):

▸
Site: gov.br/anpd
▸
Endereço: SCN, Quadra 06, Conjunto A, Bloco B — Brasília/DF
Documento em conformidade com LGPD (Lei 13.709/2018) e ECA (Lei 8.069/1990).'''

FEED = ''' Feed
Destaques
da temporada.

Os atletas que estão chamando atenção nas peneiras. Confirme os atributos que você viu em campo, vote nos destaques e siga quem quer acompanhar — tudo fica salvo neste navegador.
12 atletas · 12 estados · 5 peneiras
'''