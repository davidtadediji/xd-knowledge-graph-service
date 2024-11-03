from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI
from app.config import settings
import os


os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
llm = ChatOpenAI(temperature=0, model_name="gpt-4o-mini")


def transform_documents_to_graph(docs):
    transformer = LLMGraphTransformer(
        llm=llm,
        node_properties=True,
        relationship_properties=True,
    )
    graph_documents = transformer.convert_to_graph_documents(docs)
    print(f"Nodes:{graph_documents[0].nodes}")
    print(f"Relationships:{graph_documents[0].relationships}")
    return graph_documents
