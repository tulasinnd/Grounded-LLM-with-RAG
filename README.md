# **Grounded LLM with RAG**

## **Overview**

This project implements a Retrieval-Augmented Generation (RAG) pipeline from scratch to understand how modern NLP systems combine semantic search with language models.

Instead of relying only on a model’s internal knowledge, the system retrieves relevant information from external documents and uses it to support grounded response generation.

The current implementation focuses on building the core data pipeline, including document processing, chunking, and semantic embedding generation.

## **Architecture**

The system follows a standard Retrieval-Augmented Generation (RAG) pipeline:

```
Documents (PDF / Text)
        ↓
Text Processing (Cleaning + Chunking)
        ↓
Embedding Model (Semantic Vector Representation)
        ↓
Vector Index (FAISS)
        ↓
Query → Embedding → Similarity Search
        ↓
Top-K Relevant Chunks
        ↓
LLM (GPT-2) → Final Answer
```

This architecture separates retrieval and generation, allowing the system to access external knowledge and produce more grounded responses.

## **Components**

The current implementation includes the following modules:

* **Loader**
  Loads documents from the data directory and maintains source information.

* **Chunker**
  Splits documents into smaller overlapping chunks to preserve semantic continuity and improve retrieval quality.

* **Embedder**
  Converts each text chunk into a dense vector representation using a pretrained embedding model.

* **Config**
  Centralized configuration for controlling parameters such as chunk size, overlap, and model selection.

## **Embedding Strategy**

Each document chunk is converted into a dense vector using the `all-MiniLM-L6-v2` sentence-transformer model.

The embedding process involves:

* Tokenizing the input text (handled internally by the model)
* Encoding tokens through a transformer-based encoder
* Applying pooling to generate a fixed-size vector representation (384 dimensions)

Instead of embedding entire documents, the system operates at the chunk level. This improves retrieval granularity and allows more precise matching between user queries and relevant content.

These embeddings form a semantic vector space where:

* Similar meanings are located closer together
* Retrieval can be performed using vector similarity instead of keyword matching

This representation is the foundation for efficient and scalable information retrieval in the RAG pipeline.
