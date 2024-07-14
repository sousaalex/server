import os
import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        print(f"Mensagem recebida: {message}")
        await websocket.send(message)
        print(f"Mensagem enviada de volta: {message}")

# Get port number from environment variable (default 8765)
ws_port = int(os.environ.get("WS_PORT", 8765))

start_server = websockets.serve(echo, "0.0.0.0", ws_port)  # Listen on all interfaces

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
