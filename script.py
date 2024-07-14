import asyncio
import websockets

async def send_message():
    uri = "wss://serverproducts-9lt2.onrender.com"
    async with websockets.connect(uri) as websocket:
        await websocket.send("oi")
        print(f"> Enviado: oi")
        
        response = await websocket.recv()
        print(f"< Recebido: {response}")

# Executa o script
asyncio.get_event_loop().run_until_complete(send_message())
