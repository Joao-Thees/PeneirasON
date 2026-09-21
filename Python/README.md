# Peneiras On — CLI em Python (Sprint 3 · CTWP)

Plataforma que descentraliza a captação de talentos no futebol brasileiro: organiza
inscrição, alocação geográfica e ranking pelo olheiro. Este é o **"gêmeo lógico"** do
MVP visual — os mesmos fluxos, campos e regras, só que no terminal.

Projeto acadêmico da FIAP (1º ano de Engenharia de Software), em parceria com a Pelé Academia.

## MVP visual (site espelhado)

https://peneirason.vercel.app/

## Integrantes

| Nome | RM | Função |
|---|---|---|
| Arthur Alen Amorelli Pereira | 571897 | Front End |
| João Thees Castro Santiago | 572829 | Python |
| Caio Viana de Faria | 570634 | Edge Computing |
| Clara Diel Gama Secco | 571679 | Edge Computing |
| Anna | 573453 | Diferentiated Problem Solving |

## Como rodar

Requer Python 3 e a biblioteca **Rich**:

```bash
pip install rich
python main.py
```

Ao abrir, digite uma rota do menu (ex: `inscricao`, `feed`, `entrar`) ou `sair`.

## Estruturas de dados

- `atletas` — lista de dicionários (schema com `atributos` aninhado)
- `peneiras` — lista de dicionários
- `perfis_posicao` — dicionário de dicionários (7 posições × 8 atributos)
- `presencas` — matriz (linha = atleta, coluna = presença no check-in)
- `avaliacoes` — matriz (linha = atleta, colunas = técnica, físico, tático, atitude)

## Justificativa de imitação

1. O MVP visual usa query string para buscar o que o usuário quer visualizar/interagir.
2. Seguindo essa lógica, faz mais sentido implementar inputs validados "imitando" a query
   string. Por isso não usamos números tipo "insira [1] para isso ou [2] para aquilo".

## Arquivos (módulos)
- `docstring` — todos os módulos e códigos com docstring em cada função para entendimento rápido e produtivo tanto de uma LLM quanto de um avaliador (professor) - e também para o desenvolvedor do projeto (João Thees)
- `main.py` — integra tudo: header, login e roteamento das rotas
- `dados.py` — constantes, coleções (atletas, peneiras, matrizes…) e o estilo (borda Rich verde-limão)
- `jogador.py` — área do atleta: inscrição, feed, status e score de completude
- `olheiro.py` — painel do olheiro: lista, check-in e avaliação
- `gestora.py` — painel da gestora (academia): dashboard, mapa de calor, pipeline e peneiras
- `textos.py` — textos longos das telas institucionais (constantes)
- `prompts.txt` — registro dos prompts de IA usados no desenvolvimento
