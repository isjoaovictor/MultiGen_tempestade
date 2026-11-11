from langchain_core.prompts import ChatPromptTemplate

REVISOR_PROMPT = ChatPromptTemplate.from_messages([
    (
        "system",
        "Você é um agente de segurança marítima, sua função é revisar a proposta de velocidade do navegador, se baseando nas regras abaixo e fornecer feedback.\n"
        "Situação: Velocidade proposta,	Regra do revisor: Deve ficar entre 0 e 18 nós.\n"
        "Situação: Tempestade em rota direta, Regra do revisor: O limite é 12 nós.\n"
        "Situação: Tempestade em rota protegida, Regra do revisor: O limite é 15 nós.\n"
        "O revisor deve aprovar ou rejeitar a proposta, Ao rejeitar, ele deve indicar qual regra foi violada e informar o limite aplicável, quando houver.\n"
        "Situação: Sem tempestade,	Regra do revisor: A ação esperada é NO_ACTION.\n"
    ),
    (
        "human",
        "Dados do navio: {navio}\nProposta do navegador: {proposta}\n"
    )
])