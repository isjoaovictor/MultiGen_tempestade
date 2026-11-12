# MultiGen Tempestade

Projeto Python que simula decisões de navegação com dois agentes de IA e revisão humana. Pelo terminal, o usuário escolhe um navio e acompanha a avaliação de uma proposta de velocidade.

## Como funciona

1. **Recebimento** carrega os dados do navio selecionado.
2. **Navegador** propõe mudar a velocidade (`SET_SPEED`) ou mantê-la (`NO_ACTION`).
3. **Revisor** avalia a ação e a velocidade propostas com base na rota e na condição do tempo. Em tempestade, o limite do exercício é de **12 nós na rota direta** e **15 nós na rota protegida**.
4. **Nova tentativa** ocorre se a primeira proposta for rejeitada. O navegador usa o motivo da rejeição para preparar outra proposta.
5. **Revisão humana** ocorre após duas rejeições. O operador vê a proposta e as justificativas dos dois agentes. Ele pode rejeitar ou aprovar a proposta como exceção às regras da simulação, informando o motivo.

O LangGraph coordena o fluxo e guarda o estado durante a pausa. O navegador e o revisor usam o mesmo modelo configurado, com prompts e formatos de resposta próprios. O Pydantic valida a estrutura dessas respostas.

## Como executar

### 1. Clone o repositório e crie o ambiente virtual

```bash
git clone https://github.com/isjoaovictor/MultiGen_tempestade.git
cd MultiGen_tempestade
python -m venv .venv
```

No Windows, ative o ambiente pelo PowerShell.

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux ou macOS, ative pelo terminal.

```bash
source .venv/bin/activate
```

### 2. Instale as dependências

```bash
python -m pip install langgraph langchain-core pydantic python-dotenv
```

Instale também o pacote correspondente ao provedor que você vai usar.

| `LLM_PROVIDER` | Pacote | Variável da chave |
|---|---|---|
| `google` | `langchain-google-genai` | `GOOGLE_API_KEY` |
| `openai` | `langchain-openai` | `OPENAI_API_KEY` |
| `groq` | `langchain-groq` | `GROQ_API_KEY` |
| `anthropic` | `langchain-anthropic` | `ANTHROPIC_API_KEY` |

Por exemplo, para usar Gemini, instale a integração do Google.

```bash
python -m pip install langchain-google-genai
```

### 3. Configure o modelo

Crie um arquivo `.env` na raiz do repositório. Preencha `LLM_MODEL` com o identificador de um modelo do provedor escolhido que suporte saída estruturada. O exemplo abaixo usa Gemini.

```dotenv
LLM_PROVIDER=google
LLM_MODEL=seu_modelo_gemini
GOOGLE_API_KEY=sua_chave
```

O arquivo `.env` é ignorado pelo Git.

### 4. Rode a simulação

A partir da raiz do repositório, entre em `src` e execute o módulo principal.

```bash
cd src
python -m app.main
```

## Cenários do exercício

| Navio | Resultado esperado |
|---|---|
| `S1-FAROL` | A proposta inicial de 13 nós é rejeitada. A proposta de **12 nós** é aprovada na segunda rodada. |
| `S2-MARE` | A proposta de **15 nós** é aprovada na primeira rodada. |
| `S3-CORAL` | A ação **`NO_ACTION`** é aprovada na primeira rodada. |

## Estrutura do projeto

| Caminho | Responsabilidade |
|---|---|
| `src/app/main.py` | Menu no terminal, execução do grafo e resposta do operador. |
| `src/graph/` | Estado, nós, prompts e roteamento do fluxo. |
| `src/utils/llm_adapter.py` | Configuração do modelo usado pelos agentes. |
| `src/dados/situacao_tempestade.json` | Dados dos navios da simulação. |

