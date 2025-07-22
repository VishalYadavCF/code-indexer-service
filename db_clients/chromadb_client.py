import chromadb
import os

CHROMADB_HOST = os.getenv("CHROMADB_HOST", "localhost")
CHROMADB_PORT = int(os.getenv("CHROMADB_PORT", "8000"))

class ChromaDBClientSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ChromaDBClientSingleton, cls).__new__(cls)
            cls._instance._client = chromadb.HttpClient(host=CHROMADB_HOST, port=CHROMADB_PORT)
        return cls._instance

    @property
    def client(self):
        return self._instance._client

chromadb_singleton = ChromaDBClientSingleton()
chromadb_client = chromadb_singleton.client