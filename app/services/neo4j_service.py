from langchain_community.graphs import Neo4jGraph
from app.config import settings  # Import the settings


# Print all the details to verify
print(
    f"Neo4j Connection Details:\nURL: {settings.NEO4J_URI}\nUsername: {settings.NEO4J_USERNAME}"
)

# Initialize Neo4j graph connection using settings
graph = Neo4jGraph(
    url=settings.NEO4J_URI,
    username=settings.NEO4J_USERNAME,
    password=settings.NEO4J_PASSWORD,
)

def get_processed_keys():
    """Retrieve all processed document keys from Neo4j."""
    query = """
    MATCH (d:Document)
    RETURN d.key AS key
    """
    result = graph.query(query)
    return {record["key"] for record in result}

def mark_key_as_processed(key: str):
    """Mark a document key as processed in Neo4j."""
    query = """
    MERGE (d:Document {key: $key})
    RETURN d
    """
    graph.query(query, key=key)
