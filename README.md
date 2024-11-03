# Knowledge Graph Service

This project is a FastAPI-based service designed to process documents, transform them into graph structures, and store them in a Neo4j database. The service fetches documents from an S3 bucket, processes them using a language model, and integrates them into a knowledge graph.

## Features

- **Document Fetching**: Retrieves documents from an S3 bucket.
- **Graph Transformation**: Converts documents into graph structures using a language model.
- **Neo4j Integration**: Stores and manages graph data in a Neo4j database.
- **Error Handling**: Comprehensive logging and error handling for robust operation.

## Project Structure

- **app/**: Contains the main application code.
  - **routers/**: Defines API routes.
    - `graph_generator.py`: Handles the `/api/graph/generate` endpoint for processing documents.
  - **services/**: Contains service logic for document fetching and graph transformation.
    - `document_fetcher.py`: Fetches documents from S3.
    - `graph_transformer.py`: Transforms documents into graph structures.
    - `neo4j_service.py`: Manages interactions with the Neo4j database.
  - **utils/**: Utility modules.
    - `logger.py`: Sets up logging for the application.
  - **config.py**: Configuration settings for the application.

- **.idea/**: Contains IDE-specific settings and configurations.
- **docker-compose.yml**: Docker Compose configuration for setting up the Neo4j service.

## Setup

1. **Environment Variables**: Ensure you have a `.env` file with the necessary environment variables. Refer to `app/config.py` for required variables.

2. **Docker**: Use Docker Compose to set up the Neo4j service.
   ```bash
   docker-compose up -d
   ```

3. **Install Dependencies**: Install Python dependencies.
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**: Start the FastAPI application.
   ```bash
   uvicorn app.main:app --reload
   ```

## Usage

- **API Endpoint**: Access the API at `http://localhost:8000/api/graph/generate` to process documents and update the knowledge graph.

## Logging

The application uses a centralized logging system to capture and report errors and other significant events. Logs are output to the console.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact

For any inquiries or support, please contact the project maintainers.
