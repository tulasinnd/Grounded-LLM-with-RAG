from src.loader import load_documents
from src.chunker import chunk_documents

def main():
    documents = load_documents("documents/")
    print(len(documents))
    print("Loaded documents: ")
    print(documents)

    chunks = chunk_documents(documents)

    print("\nChunks:\n")
    for i, c in enumerate(chunks):
        print(f"{i} | {c['source']} -> {c['chunk']}\n")

if __name__ == "__main__":
    main()