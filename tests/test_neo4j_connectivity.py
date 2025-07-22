def test_neo4j_client():
    from db_clients.neo4j_client import get_neo4j_session
    try:
        with get_neo4j_session() as session:
            result = session.run("RETURN 1 AS test")
            value = result.single()["test"]
            print(f"Neo4j client is working. Test query result: {value}")
            return True
    except Exception as e:
        print(f"Neo4j client test failed: {e}")
        return False

if __name__ == "__main__":
    test_neo4j_client()

