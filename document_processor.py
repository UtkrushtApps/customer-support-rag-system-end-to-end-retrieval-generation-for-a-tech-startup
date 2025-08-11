from typing import List, Dict

def ingest_documents(document_dir: str) -> List[Dict]:
    """
    Loads and parses customer support documents from the specified directory.
    Args:
        document_dir: Directory containing support content files.
    Returns:
        List of dictionaries, each with parsed content and metadata.
    """
    pass

def preprocess_text(text: str) -> str:
    """
    Cleans up and prepares support text for downstream chunking.
    Args:
        text: Raw support content.
    Returns:
        Cleaned text string.
    """
    pass

def chunk_document(document: Dict, chunk_size: int, overlap: int = 0) -> List[Dict]:
    """
    Splits a support document into retrievable chunks of defined size and overlap.
    Args:
        document: Parsed document dictionary.
        chunk_size: Maximum size per chunk.
        overlap: Overlapped tokens/words between chunks.
    Returns:
        List of chunk dicts with content and metadata.
    """
    pass
