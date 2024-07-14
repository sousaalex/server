import asyncio
import websockets

async def get_server_response():
  async with websockets.connect("wss://serverproducts-9lt2.onrender.com", port=8080) as websocket:
    await websocket.send("oi")
    response = await websocket.recv()
    return response

async def main():
  server_response = await get_server_response()
  print(f"Resposta do servidor: {server_response}")

asyncio.run(main())
