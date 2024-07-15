import asyncio
import websockets
import json

async def test():
    uri = "ws://localhost:8765"
    request = {
        "categories": [
            "Kids_kits",
            "Wedding",
            "Christening_Birthday_gifts",
            "Birthday_gifts",
            "Valentines_Day",
            "Father_Day",
            "Mother_Day",
            "Christmas",
            "Caketopper",
        ],
        "price_ranges": ["0-50", "50-100", "100-200", "200+"]
    }
    
    async with websockets.connect(uri, timeout=10) as websocket:
        await websocket.send(json.dumps(request))
        print(f"> Enviado: {json.dumps(request)}")

        response = await websocket.recv()
        print(f"< Recebido: {response}")
        return response  # Retorna a resposta recebida do WebSocket

asyncio.run(test())
