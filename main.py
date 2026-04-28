import config
from src.loader import load_documents
from src.chunker import chunk_documents

def main():
    documents = load_documents(config.DOCUMENTS_PATH)

    chunks = chunk_documents(
        documents,
        chunk_size=config.CHUNK_SIZE,
        overlap=config.CHUNK_OVERLAP
    )

    print(f"Total chunks: {len(chunks)}")

if __name__ == "__main__":
    main()