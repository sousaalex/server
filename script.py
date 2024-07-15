import asyncio
import websockets
from aiohttp import web
import json

async def send_message():
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
    
    for attempt in range(5):
        try:
            async with websockets.connect(uri, timeout=10) as websocket:
                await websocket.send(json.dumps(request))
                print(f"> Enviado: {json.dumps(request)}")

                response = await websocket.recv()
                print(f"< Recebido: {response}")
                return response  # Retorna a resposta recebida do WebSocket

        except (websockets.exceptions.InvalidURI, websockets.exceptions.InvalidHandshake, websockets.exceptions.ConnectionClosedError) as e:
            print(f"Falha na tentativa {attempt + 1}: {e}")
            await asyncio.sleep(5)
        except asyncio.TimeoutError:
            print(f"Tentativa {attempt + 1} de conexão expirou.")
            await asyncio.sleep(5)

    print("Não foi possível conectar ao servidor WebSocket após várias tentativas.")
    return None  # Retorna None se não conseguir conectar

async def handle(request):
    response = await send_message()  # Chama a função para enviar a mensagem via WebSocket
    if response:
        return web.Response(text=f"Resposta do WebSocket: {response}")
    else:
        return web.Response(text="Falha ao conectar ao servidor WebSocket.")

async def init_app():
    app = web.Application()
    app.router.add_get('/', handle)
    return app

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    app = loop.run_until_complete(init_app())
    web.run_app(app, port=8000)
