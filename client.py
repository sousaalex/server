import asyncio
import websockets

async def send_message():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = "kitket!" 
        await websocket.send(message)
        print(f"Mensagem enviada: {message}")
        
        response = await websocket.recv()
        print(f"Resposta recebida: {response}")

asyncio.get_event_loop().run_until_complete(send_message())
