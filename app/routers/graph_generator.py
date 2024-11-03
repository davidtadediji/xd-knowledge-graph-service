from fastapi import APIRouter, HTTPException
from app.services.document_fetcher import fetch_parsed_documents
from app.services import neo4j_service
from app.services.graph_transformer import transform_documents_to_graph
from langchain_core.documents import Document
from app.utils.logger import logger
import botocore.exceptions
from app.config import settings

router = APIRouter(prefix="/api/graph", tags=["Graph Generator"])

graph = neo4j_service.graph

@router.post("/generate")
async def process_documents(prefix: str = ""):
    try:
        # Fetch documents from S3
        raw_documents = fetch_parsed_documents(prefix)

        if not raw_documents:
            return {"message": "No new documents to process."}

        # Convert raw documents to Document objects
        documents = [Document(page_content=doc["content"]) for doc in raw_documents]

        for doc, raw_doc in zip(documents, raw_documents):
            # Print the document content
            # print(f"Converting document to graph: {raw_doc['key']}")
            # print(f"Content: {doc.page_content}")

            # Transform document into graph document
            graph_document = transform_documents_to_graph([doc])

            # Store graph document in Neo4j
            graph.add_graph_documents(graph_document)

            # Mark the document as processed
            neo4j_service.mark_key_as_processed(raw_doc["key"])

        return {"message": f"{len(documents)} new documents processed and added to the knowledge graph."}
    except botocore.exceptions.BotoCoreError as e:
        logger.error(f"S3 error: {str(e)}")
        raise HTTPException(
            status_code=500, detail="Failed to fetch documents from S3."
        )
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")
