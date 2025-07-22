import os

import redis


def test_redis_connection():
    host = os.getenv("REDIS_HOST", "localhost")
    port = int(os.getenv("REDIS_PORT", 6379))
    try:
        r = redis.Redis(host=host, port=port)
        r.ping()
        print(f"Successfully connected to Redis at {host}:{port}")
        return True
    except Exception as e:
        print(f"Failed to connect to Redis: {e}")
        return False


def test_redis_client():
    from db_clients.redis_client import redis_client

    try:
        redis_client.ping()
        print("Redis client is working (ping successful)")
        return True
    except Exception as e:
        print(f"Redis client test failed: {e}")
        return False


if __name__ == "__main__":
    test_redis_connection()
    test_redis_client()
