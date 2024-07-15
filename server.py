import asyncio
import websockets
from firebase_admin import credentials, db, initialize_app
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Firebase Admin SDK
def initialize_firebase():
    try:
        firebase_config_json = os.getenv("FIREBASE_CONFIG_JSON")
        if firebase_config_json is None:
            raise ValueError("Firebase configuration not found in environment variables")
        
        firebase_config = json.loads(firebase_config_json)
        
        # Initialize Firebase Admin SDK with credentials and databaseURL
        cred = credentials.Certificate(firebase_config)
        initialize_app(cred, {
            'databaseURL': os.getenv("DATABASE_URL")
        })
        
        print("Firebase initialized successfully")
    except json.JSONDecodeError as e:
        raise ValueError("Invalid JSON format in FIREBASE_CONFIG_JSON variable") from e
    except ValueError as e:
        raise ValueError(f"Error initializing Firebase: {e}")

# Call the function to initialize Firebase
initialize_firebase()

async def get_data_from_firebase(categories, price_ranges):
    try:
        all_products = []

        if categories and price_ranges:
            # Caso 1: Enviar ambos (categorias e faixas de preço)
            for category in categories:
                ref = db.reference(f"/products/{category}")
                data = ref.get()

                if data:
                    for product_id, product_data in data.items():
                        product_price = float(product_data.get('productPrice', 0))
                        for price_range in price_ranges:
                            min_price, max_price = parse_price_range(price_range)
                            if (min_price is None or product_price >= min_price) and (max_price is None or product_price <= max_price):
                                all_products.append({
                                    "id": product_id,
                                    "productName": product_data.get('productName', ''),
                                    "productDescription": product_data.get('productDescription', ''),
                                    "productPhoto": product_data.get('productPhoto', ''),
                                    "productPrice": product_price
                                })
                                break

        elif categories:
            # Caso 2: Enviar apenas categorias
            for category in categories:
                ref = db.reference(f"/products/{category}")
                data = ref.get()

                if data:
                    for product_id, product_data in data.items():
                        product_price = float(product_data.get('productPrice', 0))
                        all_products.append({
                            "id": product_id,
                            "productName": product_data.get('productName', ''),
                            "productDescription": product_data.get('productDescription', ''),
                            "productPhoto": product_data.get('productPhoto', ''),
                            "productPrice": product_price
                        })

        elif price_ranges:
            # Caso 3: Enviar apenas faixas de preço
            all_categories = [
                "Kids_kits",
                "Wedding",
                "Christening_Birthday_gifts",
                "Birthday_gifts",
                "Valentines_Day",
                "Father_Day",
                "Mother_Day",
                "Christmas",
                "Caketopper",
            ]

            for category in all_categories:
                ref = db.reference(f"/products/{category}")
                data = ref.get()

                if data:
                    for product_id, product_data in data.items():
                        product_price = float(product_data.get('productPrice', 0))
                        for price_range in price_ranges:
                            min_price, max_price = parse_price_range(price_range)
                            if (min_price is None or product_price >= min_price) and (max_price is None or product_price <= max_price):
                                all_products.append({
                                    "id": product_id,
                                    "productName": product_data.get('productName', ''),
                                    "productDescription": product_data.get('productDescription', ''),
                                    "productPhoto": product_data.get('productPhoto', ''),
                                    "productPrice": product_price
                                })
                                break

        return all_products

    except Exception as e:
        print(f"Error fetching data from Firebase: {e}")
        return []

def parse_price_range(price_range):
    try:
        if '-' in price_range:
            min_price, max_price = map(float, price_range.split('-'))
            return min_price, max_price
        elif price_range.endswith('+'):
            min_price = float(price_range[:-1])
            return min_price, None
        else:
            return None, None
    except ValueError:
        return None, None

async def handler(websocket, path):
    async for message in websocket:
        try:
            print(f"Received message: {message}")  # Debug log
            request = json.loads(message)
            
            categories = request.get('categories', [])
            price_ranges = request.get('price_ranges', [])
            
            if not isinstance(categories, list) or not isinstance(price_ranges, list):
                await websocket.send(json.dumps({"error": "Invalid message format, expected lists"}))
                continue
            
            products = await get_data_from_firebase(categories, price_ranges)
            await websocket.send(json.dumps(products))
        
        except websockets.ConnectionClosed:
            print("Connection closed")
            break
        
        except Exception as e:
            print(f"Error handling message: {e}")
            await websocket.send(json.dumps({"error": "Internal server error"}))

async def main():
    ws_port = int(os.environ.get("WS_PORT", 8765))
    print(f"Starting WebSocket server on port {ws_port}...")

    async with websockets.serve(handler, "0.0.0.0", ws_port):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
