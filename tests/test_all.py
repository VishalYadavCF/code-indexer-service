import os
from dotenv import load_dotenv

# Explicitly load .env from project root
load_dotenv(dotenv_path=os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env'))

from tests import test_chromadb_connectivity, test_redis_connectivity, test_mongo_connectivity, test_neo4j_connectivity

def run_all_tests():
    print("Running ChromaDB connectivity tests...")
    test_chromadb_connectivity.test_chromadb_connection()
    test_chromadb_connectivity.test_chromadb_client()

    print("\nRunning Redis connectivity tests...")
    test_redis_connectivity.test_redis_connection()
    test_redis_connectivity.test_redis_client()

    print("\nRunning MongoDB connectivity tests...")
    test_mongo_connectivity.test_mongo_client()

    print("\nRunning Neo4j connectivity tests...")
    test_neo4j_connectivity.test_neo4j_client()

if __name__ == "__main__":
    run_all_tests()
