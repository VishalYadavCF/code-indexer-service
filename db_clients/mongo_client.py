import os

from pymongo import MongoClient

MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
DB_NAME = os.getenv("MONGO_DB_NAME")

MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"


class MongoClientSingleton:
    _instance = None
    _db = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoClientSingleton, cls).__new__(cls)
            cls._instance.client = MongoClient(MONGO_URI)
            cls._db = cls._instance.client[DB_NAME]
        return cls._instance

    @property
    def db(self):
        return self._db


mongo_singleton = MongoClientSingleton()
db = mongo_singleton.db

# Collections
repo_metadata = db["repo_metadata"]
node_summaries = db["node_summaries"]
prompts = db["prompts"]
tool_configs = db["tool_configs"]

# Utility functions


def insert_repo_metadata(data):
    return repo_metadata.insert_one(data)


def find_repo_metadata(query):
    return list(repo_metadata.find(query))


def insert_node_summary(data):
    return node_summaries.insert_one(data)


def find_node_summaries(query):
    return list(node_summaries.find(query))


def insert_prompt(data):
    return prompts.insert_one(data)


def find_prompts(query):
    return list(prompts.find(query))


def insert_tool_config(data):
    return tool_configs.insert_one(data)


def find_tool_configs(query):
    return list(tool_configs.find(query))


def upsert_index_metadata(
    index_id, git_repo, project_name, index_status, index_meta=None
):
    from datetime import datetime

    if index_meta is None:
        index_meta = []
    now = datetime.utcnow()
    result = repo_metadata.update_one(
        {"id": index_id},
        {
            "$set": {
                "id": index_id,
                "git_repo": git_repo,
                "project_name": project_name,
                "index_status": index_status,
                "index_meta": index_meta,
                "updated_at": now,
            },
            "$setOnInsert": {"created_at": now},
        },
        upsert=True,
    )
    return result
