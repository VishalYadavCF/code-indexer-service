import os

import requests


def test_chromadb_connection():
    import socket

    host = os.getenv("CHROMADB_HOST", "localhost")
    port = int(os.getenv("CHROMADB_PORT", 8000))
    try:
        with socket.create_connection((host, port), timeout=5):
            print(f"Successfully connected to ChromaDB TCP socket at {host}:{port}")
            return True
    except Exception as e:
        print(f"Failed to connect to ChromaDB TCP socket: {e}")
        return False


def test_chromadb_client():
    from db_clients.chromadb_client import chromadb_client

    try:
        # Try listing collections (or another simple operation)
        collections = chromadb_client.list_collections()
        print(f"ChromaDB client is working. Collections: {collections}")
        return True
    except Exception as e:
        print(f"ChromaDB client test failed: {e}")
        return False


if __name__ == "__main__":
    test_chromadb_connection()
    test_chromadb_client()
