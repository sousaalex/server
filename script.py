import asyncio
import websockets

async def send_message():
    uri = "wss://serverproducts-9lt2.onrender.com"
    
    # Tenta conectar várias vezes
    for attempt in range(5):
        try:
            async with websockets.connect(uri, timeout=10) as websocket:
                await websocket.send("oiAlex")
                print(f"> Enviado: oi")

                response = await websocket.recv()
                print(f"< Recebido: {response}")
                return  # Conexão bem-sucedida, sair da função

        except (websockets.exceptions.InvalidURI, websockets.exceptions.InvalidHandshake, websockets.exceptions.ConnectionClosedError) as e:
            print(f"Falha na tentativa {attempt + 1}: {e}")
            await asyncio.sleep(5)  # Espera 5 segundos antes de tentar novamente
        except asyncio.TimeoutError:
            print(f"Tentativa {attempt + 1} de conexão expirou.")
            await asyncio.sleep(5)

    print("Não foi possível conectar ao servidor WebSocket após várias tentativas.")

# Executa o script
asyncio.run(send_message())
