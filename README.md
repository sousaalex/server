# WebSocket Server and Client Example

This repository contains a simple example of a WebSocket server and client implemented in Python using `asyncio` and `websockets`.

## Table of Contents

- [WebSocket Server and Client Example](#websocket-server-and-client-example)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Files](#files)
  - [WebSocket Server (`server.py`)](#websocket-server-serverpy)
    - [Setup](#setup)
    - [Running the Server](#running-the-server)
  - [WebSocket Client (`client.py`)](#websocket-client-clientpy)
    - [Setup](#setup-1)
    - [Running the Client](#running-the-client)
  - [Notes](#notes)
  - [License](#license)

## Overview

This repository provides a basic example of a WebSocket server and client implementation in Python. The server listens on port `8765` and echoes messages received from clients back to them. The client connects to the server, sends a predefined message, and prints the response received from the server.

## Files

- `server.py`: WebSocket server script.
- `client.py`: WebSocket client script.

## WebSocket Server (`server.py`)

The WebSocket server listens on port `8765` and echoes messages received from clients back to them.

### Setup

Make sure you have Python 3.6+ installed.

### Running the Server

To start the WebSocket server, run:

```bash
python server.py


