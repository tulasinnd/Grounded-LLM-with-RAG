def chunk_documents(documents, chunk_size=200, overlap=50):
    chunks = []

    for doc in documents:
        text = doc["text"]
        source = doc["source"]

        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunks.append({
                "chunk": chunk_text,
                "source": source
            })

            start += chunk_size - overlap

    return chunks