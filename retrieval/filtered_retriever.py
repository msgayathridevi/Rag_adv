import pickle

with open("chunks.pkl", "rb") as f:
    chunks = pickle.load(f)


def filter_chunks(access_level):

    if access_level == "all":
        return chunks

    return [
        chunk
        for chunk in chunks
        if chunk["access_level"] == access_level
    ]