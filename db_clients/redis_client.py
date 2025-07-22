import os

import redis

REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")


class RedisClientSingleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RedisClientSingleton, cls).__new__(cls)
            cls._instance._client = redis.from_url(REDIS_URL)
        return cls._instance

    @property
    def client(self):
        return self._instance._client


redis_singleton = RedisClientSingleton()
redis_client = redis_singleton.client

# Pub/Sub utility


def publish(channel, message):
    redis_client.publish(channel, message)


def subscribe(channel):
    pubsub = redis_client.pubsub()
    pubsub.subscribe(channel)
    return pubsub


# For Celery, set REDIS_URL as broker and backend in your celery config
# Example:
# celery_app = Celery('tasks', broker=REDIS_URL, backend=REDIS_URL)
