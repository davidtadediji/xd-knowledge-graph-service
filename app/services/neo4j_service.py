from langchain_community.graphs import Neo4jGraph
from app.config import settings
from app.utils.logger import logger  # Import the central logger

# Initialize Neo4j graph connection using settings
graph = Neo4jGraph(
    url=settings.NEO4J_URI,
    username=settings.NEO4J_USERNAME,
    password=settings.NEO4J_PASSWORD,
)

def get_processed_keys():
    """Retrieve all processed document keys from Neo4j."""
    try:
        query = """
        MATCH (d:Document)
        RETURN d.key AS key
        """
        result = graph.query(query)
        return {record["key"] for record in result}
    except Exception as e:
        logger.warning(f"Could not retrieve any processed keys: {str(e)}")
        return set()  # Return an empty set if there's an error

def mark_key_as_processed(key: str):
    """Mark a document key as processed in Neo4j."""
    query = """
    MERGE (d:Document {key: $key})
    RETURN d
    """
    graph.query(query, params={"key": key})
