### WebSocket Server and Client for Fetching Products from Firebase

This repository contains Python scripts for setting up a WebSocket server and client to retrieve product data from Firebase based on categories and price ranges.

#### Server Side (`server.py`)

The server script (`server.py`) sets up a WebSocket server using `asyncio` and `websockets`. It interacts with Firebase to fetch product data based on provided categories and price ranges.

**Dependencies:**
- `asyncio`: Python's asynchronous I/O library.
- `websockets`: Async WebSocket server and client library.
- `firebase_admin`: Python SDK for Firebase.
- `dotenv`: Module for loading environment variables from a `.env` file.

**Firebase Integration:**
- Initializes Firebase using credentials provided in a JSON format stored in environment variables.
- Defines a function to fetch product data from Firebase based on categories and/or price ranges.
- Handles different combinations of categories and price ranges to filter products accordingly.

**WebSocket Server:**
- Listens for incoming WebSocket connections on a specified port (`WS_PORT`).
- Handles incoming messages from clients (JSON format) containing categories and price ranges.
- Sends back JSON responses containing product details matching the requested criteria.

#### Client Side (`client.py`)

The client script (`client.py`) connects to the WebSocket server (`server.py`) to request product data based on predefined categories and price ranges.

**Dependencies:**
- `asyncio`: Python's asynchronous I/O library.
- `websockets`: Async WebSocket server and client library.

**WebSocket Client:**
- Connects to the WebSocket server running locally (`ws://localhost:8765`).
- Sends a JSON message containing categories and price ranges.
- Receives and prints the response from the server, which includes product details.

#### Usage

1. **Server Setup:**
   - Ensure Python dependencies (`asyncio`, `websockets`, `firebase_admin`, `dotenv`) are installed.
   - Set up a Firebase project and obtain credentials (`FIREBASE_CONFIG_JSON`) and database URL (`DATABASE_URL`).
   - Store Firebase credentials in a `.env` file.
   - Run `server.py` to start the WebSocket server.

2. **Client Setup:**
   - Install dependencies (`asyncio`, `websockets`).
   - Modify the `request` JSON in `client.py` to specify desired categories and price ranges.
   - Run `client.py` to connect to the WebSocket server and fetch product data.

#### Example Request (`client.py`)

```python
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
