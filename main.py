import faiss
import numpy as np

import config
from src.chunker import chunk_documents
from src.embedder import Embedder
from src.generator import Generator
from src.loader import load_documents


def main():
    # Load documents
    documents = load_documents(config.DOCUMENTS_PATH)

    # Create chunks
    chunks = chunk_documents(
        documents,
        chunk_size=config.CHUNK_SIZE,
        overlap=config.CHUNK_OVERLAP,
    )

    # Generate embeddings
    embedder = Embedder(config.EMBEDDING_MODEL)

    chunk_texts = [chunk["chunk"] for chunk in chunks]
    embeddings = embedder.encode(chunk_texts)

    # Attach embeddings to chunks
    for chunk, embedding in zip(chunks, embeddings):
        chunk["embedding"] = embedding

    # Build FAISS index
    embedding_matrix = np.array(
        [chunk["embedding"] for chunk in chunks],
        dtype=np.float32,
    )

    index = faiss.IndexFlatL2(embedding_matrix.shape[1])
    index.add(embedding_matrix)

    # Query
    print("\nSample questions related to documents:")
    print("- Who is the AI assistant used by employees?")
    print("- What is the most popular product?")
    print("- Which product was released in 2025?")
    print("- What does NovaSecure do?\n")

    query = input("Enter your question: ")
    query_embedding = embedder.encode([query])

    # Retrieve relevant chunks
    k = 2
    _, indices = index.search(query_embedding, k)
    retrieved_chunks = [chunks[i] for i in indices[0]]

    print("Retrieved Context:")
    for i, chunk in enumerate(retrieved_chunks, start=1):
        print(f"\nChunk {i}:")
        print(chunk["chunk"])

    # Generate answer
    generator = Generator(config.GENERATOR_MODEL)

    context = "\n".join(chunk["chunk"] for chunk in retrieved_chunks)

    prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{query}

Answer in one or two sentences:
"""

    answer = generator.generate(prompt)

    print("\n\nGenerated Answer:")
    print(answer)


if __name__ == "__main__":
    main()