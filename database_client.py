from typing import Any, Dict, Optional

class ChromaDBClient:
    """
    Initializes and manages connection to Chroma DB at localhost:8000 for vector operations.
    """
    def __init__(self, config: Dict[str, Any]) -> None:
        pass

    def create_collection(self, name: str, metadata_schema: Optional[Dict[str, Any]] = None) -> None:
        pass

    def insert_vectors(self, collection: str, vectors: list, metadatas: Optional[list] = None) -> None:
        pass

    def query(self, collection: str, vector: list, top_k: int = 5) -> list:
        pass

    def close(self) -> None:
        pass
