import config
from src.loader import load_documents
from src.chunker import chunk_documents
from src.embedder import Embedder

def main():
    # LOADING
    # load documents
    documents = load_documents(config.DOCUMENTS_PATH)
    print(documents)

    # CHUNKING
    # create chunks from documents
    chunks = chunk_documents(
        documents,
        chunk_size=config.CHUNK_SIZE,
        overlap=config.CHUNK_OVERLAP )
    print(f"Total chunks: {len(chunks)}")
    print(chunks)

    # EMBEDDING
    # initialize embedder
    embedder = Embedder(config.EMBEDDING_MODEL)

    # extract chunk texts
    chunk_texts = [c["chunk"] for c in chunks]

    # generate embeddings
    embeddings = embedder.encode(chunk_texts)
    print(embeddings)
    print(len(embeddings))        # number of chunks
    print(len(embeddings[0]))     # embedding dimension

    # attach embeddings back to chunks
    for i, emb in enumerate(embeddings):
        chunks[i]["embedding"] = emb
    print(chunks)

if __name__ == "__main__":
    main()