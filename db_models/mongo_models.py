from datetime import datetime
from enum import Enum
from typing import List, Optional

from pydantic import BaseModel


class IndexMetaItem(BaseModel):
    key: str
    value: str
    # You can expand this as needed


class IndexMetadataResponse(BaseModel):
    id: str
    git_repo: str
    project_name: str
    index_status: str
    index_meta: List[IndexMetaItem] = []
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class RepoMetadata(BaseModel):
    id: str
    repo_name: str
    neo4j_index_id: Optional[str] = None
    repo_git_link: Optional[str] = None
    # Add more fields as needed
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class Neo4jNodeSummary(BaseModel):
    id: str
    node_id: str
    entity_type: str  # e.g., class, interface, method, etc
    semantic_summary: Optional[str] = None
    discovery_questions: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class LLMPrompt(BaseModel):
    id: str
    prompt_name: str
    prompt_content: str
    prompt_version: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None


class NodeType(str, Enum):
    FUNCTION = "Function"
    CLASS = "Class"
    FILE = "File"
    MODULE = "Module"
    VARIABLE = "Variable"
    PROJECT = "Project"
    PACKAGE = "Package"
    DEPENDENCIES = "Dependencies"


class RelationshipType(str, Enum):
    CALLS = "CALLS"
    CONTAINS = "CONTAINS"
    IMPORTS = "IMPORTS"
    EXTENDS = "EXTENDS"
    USES = "USES"
    DEPENDS_ON = "DEPENDS_ON"  # For package/file dependency


class CodeNode(BaseModel):
    node_id: str
    node_type: NodeType
    name: str
    repo_id: str
    file_path: str
    start_line: int
    end_line: int
    text: str
    docstring: Optional[str] = None
    embedding: Optional[List[float]] = []
    labels: Optional[List[str]] = []


class CodeRelationship(BaseModel):
    start_node_id: str
    end_node_id: str
    relationship_type: RelationshipType
