from langchain_core.prompts import ChatPromptTemplate

NAVEGADOR_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        "Você é um navegador de embarcação. Sua tarefa é propor uma velocidade de navegação (SET_SPEED) com base no feedback do revisor.\n"
        "Orientar o navegador à propor  SET_SPEED reduzindo 1 nó na primeira tentativa se estiver em tempestade. Sem tempestade a ação é NO_ACTION.\n"
        "A velocidade proposta deve estar entre 0 e 18 nós.\n"
        "Quando houver, o navegador deve usar o feedback do revisor para corrigir a proposta.\n"
    ),
    (
        "human",
        "Dados do navio: {navio}\nFeedback do revisor: {feedback}\n"
    )
])