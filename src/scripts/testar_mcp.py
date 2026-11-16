import asyncio

from src.utils.mcp_client import get_tools_by_name, parse_result


async def main() -> None:
    tools = await get_tools_by_name()
    set_speed = tools["set_speed"]

    async def chamar(ship, kn, versao, chave):
        raw = await set_speed.ainvoke(
            {"ship_id": ship, "speed_kn": kn, "expected_state_version": versao, "idempotency_key": chave}
        )
        return parse_result(raw)

    print("1", await chamar("S1-FAROL", 12, 1, "treino:S1-FAROL:SET_SPEED:v1"))
    print("2", await chamar("S1-FAROL", 12, 1, "treino:S1-FAROL:SET_SPEED:v1"))
    print("3", await chamar("S1-FAROL", 11, 1, "outra-chave"))
    print("4", await chamar("S1-FAROL", 12.3, 2, "chave-3"))


if __name__ == "__main__":
    asyncio.run(main())