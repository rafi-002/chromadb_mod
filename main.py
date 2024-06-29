from fastapi import FastAPI, Query
from pydantic import BaseModel
import chromadb
from chromadb.utils import embedding_functions
from data_loader import load_data
from chroma_db import initialize_collection, query_collection       
import uvicorn
from config import function_name

app = FastAPI()

# Load data and initialize ChromaDB
documents, metadata, ids = load_data("Data_2_Formatted.xlsx")

# Create the embeddings
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name= function_name
)

# Store the embeddings in ChromaDB
client = chromadb.PersistentClient()
collection = initialize_collection(client, "crop_data", embedding_func, documents, metadata, ids)

# Define the query model
class QueryModel(BaseModel):
    query: str

# Define the query endpoint that accepts the query as a JSON object in the request body
@app.post("/query/")
async def query_json(data: QueryModel):
    results = query_collection(collection, data.query)
    return results

# Define the query endpoint that accepts the query as a query parameter in the URL
@app.get("/query/")
async def query_url(query: str = Query(...)):
    results = query_collection(collection, query)
    return results

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
