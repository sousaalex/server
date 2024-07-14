import os
import asyncio
import websockets

async def send_message():
    # Obtém o número da porta da variável de ambiente PORT ou usa 443 (porta padrão para WebSocket seguro)
    ws_port = int(os.environ.get("PORT", 443))
    uri = f"wss://serverproducts-9lt2.onrender.com:{ws_port}"
    async with websockets.connect(uri) as websocket:
        await websocket.send("oi")
        print(f"> Enviado: oi")
        
        response = await websocket.recv()
        print(f"< Recebido: {response}")

# Executa o script
asyncio.run(send_message())
