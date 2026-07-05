import streamlit as st
import faiss
import numpy as np

import config
from src.chunker import chunk_documents
from src.embedder import Embedder
from src.generator import Generator
from src.loader import load_documents

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="RAG Knowledge Base",
    page_icon="📄",
    layout="wide"
)

# -------------------------------------------------
# Header
# -------------------------------------------------

st.markdown(
    """
    <h1 style="text-align:center;">
        📄 RAG Knowledge Base Chatbot
    </h1>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <p style="text-align:center;font-size:18px;">
        Upload a PDF and ask questions about its content using Retrieval-Augmented Generation (RAG).
    </p>
    """,
    unsafe_allow_html=True,
)

st.divider()

# -------------------------------------------------
# Build Pipeline
# -------------------------------------------------

@st.cache_resource
def build_pipeline(uploaded_file):

    documents = load_documents(uploaded_file)

    chunks = chunk_documents(
        documents,
        chunk_size=config.CHUNK_SIZE,
        overlap=config.CHUNK_OVERLAP,
    )

    embedder = Embedder(config.EMBEDDING_MODEL)

    chunk_texts = [chunk["chunk"] for chunk in chunks]
    embeddings = embedder.encode(chunk_texts)

    for chunk, embedding in zip(chunks, embeddings):
        chunk["embedding"] = embedding

    embedding_matrix = np.array(
        [chunk["embedding"] for chunk in chunks],
        dtype=np.float32,
    )

    index = faiss.IndexFlatL2(embedding_matrix.shape[1])
    index.add(embedding_matrix)

    generator = Generator(config.GENERATOR_MODEL)

    return chunks, embedder, index, generator


# -------------------------------------------------
# Two Column Layout
# -------------------------------------------------

#left_col, right_col = st.columns([1, 2])
left_col, space, right_col = st.columns([1, 0.2, 2])

answer = None
retrieved_chunks = []

with left_col:

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    question = st.text_input(
        "",
        placeholder="ASK: e.g. What is the most popular product?"
    )

    ask = st.button(
        "🔍 Generate Answer",
        use_container_width=True
    )


# -------------------------------------------------
# Generate Answer
# -------------------------------------------------

if uploaded_file is not None:

    chunks, embedder, index, generator = build_pipeline(uploaded_file)

    if ask and question:

        with st.spinner("Searching knowledge base..."):

            query_embedding = embedder.encode([question])

            _, indices = index.search(query_embedding, 2)

            retrieved_chunks = [
                chunks[i]
                for i in indices[0]
            ]

            context = "\n".join(
                chunk["chunk"]
                for chunk in retrieved_chunks
            )

            prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}

Answer in one or two sentences:
"""

            answer = generator.generate(prompt)


# -------------------------------------------------
# Right Panel
# -------------------------------------------------

with right_col:

    # st.subheader("🤖 Generated Answer")
    st.markdown(
    """
    <p style="text-align:center;font-size:16px;">
        Generated Answer
    </p>
    """,
    unsafe_allow_html=True,)

    if answer:

        st.success(answer)

        # with st.expander("Retrieved Context"):

        #     for i, chunk in enumerate(retrieved_chunks, start=1):

        #         st.markdown(f"**Chunk {i}**")
        #         st.info(chunk["chunk"])

    else:

        st.info(
            "Upload a PDF, enter a question, and click **Generate Answer**."
        )