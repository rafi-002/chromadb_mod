import chromadb
from chromadb.utils import embedding_functions
from config import collection_name

def initialize_collection(client, name, embedding_func, documents, metadata, ids):
  
    existing_collections = client.list_collections()

    for coll in existing_collections:
        if coll.name == name:
            print(f"Using Existing Collectiion {name}")
            return client.get_collection(name)
    else:   
        collection =  client.create_collection(
            name=name,
            embedding_function=embedding_func,
            metadata={"hnsw:space": "cosine"}
        )
        collection.add(documents=documents, metadatas=metadata, ids=ids)

    return collection

def query_collection(collection, query_text, n_results=3):
    results = collection.query(query_texts=[query_text], n_results=n_results)
    return results
