import pandas as pd

def load_data(file_path):
    data = pd.read_excel(file_path)
    documents = data["Message"].tolist()
    metadata = [{"title": row["Title"], "tag": row["Tag"]} for _, row in data.iterrows()]
    ids = [str(i) for i in data.index.tolist()]
    return documents, metadata, ids
