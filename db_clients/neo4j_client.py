import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

NEO4J_URI = os.getenv("NEO4J_URI")
NEO4J_USER = os.getenv("NEO4J_USER")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

load_dotenv()

class Neo4jClientSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Neo4jClientSingleton, cls).__new__(cls)
            cls._instance.driver = GraphDatabase.driver(
                NEO4J_URI,
                auth=(NEO4J_USER, NEO4J_PASSWORD)
            )
        return cls._instance

    def get_session(self):
        return self.driver.session()

neo4j_client_singleton = Neo4jClientSingleton()

def get_neo4j_session():
    return neo4j_client_singleton.get_session()

if __name__ == "__main__":
    try:
        with get_neo4j_session() as session:
            result = session.run("RETURN 1 AS test")
            print("Neo4j connection test result:", result.single()["test"])
    except Exception as e:
        print("Neo4j connection failed:", e)
