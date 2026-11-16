import asyncio

from dotenv import load_dotenv
from src.graph.state import State
from src.graph.builder import graph
from langgraph.types import Command


async def main():
    load_dotenv()

    while True:
        escolha_navio = input(
            "\nEscolha um navio para a simulação:\n"
            "1. S1-FAROL\n"
            "2. S2-MARE\n"
            "3. S3-CORAL\n"
            "Escolha (1-3): "
        ).strip()

        match escolha_navio:
            case "1":
                ship_id = "S1-FAROL"
            case "2":
                ship_id = "S2-MARE"
            case "3":
                ship_id = "S3-CORAL"
            case _:
                print("Opção inválida. Tente novamente.")
                continue
        break

    estado_inicial: State = {
        "ship_id": ship_id,
        "rodada": 0,
        "tentativas": 0,
    }

    config = {
        "configurable": {
            "thread_id": "frota-1"
        }
    }

    resposta = await graph.ainvoke(
        estado_inicial,
        config=config
    )

    pausas = resposta.get("__interrupt__", [])

    if pausas:
        print(pausas[0].value)

        retorno = input(
            "\nDeseja continuar? (s/n): "
        ).strip().lower()

        while retorno not in ["s", "n"]:
            retorno = input(
                "\nOpção inválida. Deseja continuar? (s/n): "
            ).strip().lower()

        motivo = ""

        if retorno == "s":
            motivo = input(
                "\nDigite o motivo da exceção: "
            ).strip()

        resposta = await graph.ainvoke(
            Command(
                resume=retorno == "s",
                update={"motivo_excecao": motivo},
            ),
            config=config
        )

    print(resposta["resultado"])


if __name__ == "__main__":
    asyncio.run(main())
