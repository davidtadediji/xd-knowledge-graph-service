import boto3
from app.config import settings
from app.services import neo4j_service 

s3_client = boto3.client(
    "s3",
    aws_access_key_id=settings.S3_ACCESS_KEY,
    aws_secret_access_key=settings.S3_SECRET_KEY,
    region_name=settings.S3_REGION,
)

def fetch_parsed_documents(prefix=""):
    """Fetch new parsed documents from S3 bucket."""
    documents = []
    response = s3_client.list_objects_v2(Bucket=settings.S3_BUCKET, Prefix=prefix)

    # Get list of already processed keys from Neo4j
    processed_keys = neo4j_service.get_processed_keys()

    for obj in response.get("Contents", []):
        file_key = obj["Key"]
        if file_key in processed_keys:
            continue  # Skip already processed documents

        file_obj = s3_client.get_object(Bucket=settings.S3_BUCKET, Key=file_key)
        content = file_obj["Body"].read().decode("utf-8")
        documents.append({"key": file_key, "content": content})  # Store key with content
        print(f"Fetched document: {file_key}")
    return documents
