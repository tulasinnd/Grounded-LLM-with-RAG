def chunk_documents(documents, chunk_size, overlap):
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

'''
Example chunks:

Total chunks: 5

[{'chunk': 'Transformers are powerful models in NLP.\nThey use attention mechanisms.\nRAG combines retrieval with generation.',
 'source': 'sample.txt'}, 
 
 {'chunk': '"You don\'t have to be French to enjoy a decent red wine," Charles Jousselin de Gruse used to tell his foreign 
 guests whenever he entertained them in Paris. "But you do have to be French to recognize o', 
 'source': 'sample1.txt'}, 
 
 {'chunk': 'aris. "But you do have to be French to recognize one," he would add with a laugh.\n\nAfter a lifetime in the French 
 diplomatic corps, the Count de Gruse lived with his wife in an elegant townhouse on Qu', 
 'source': 'sample1.txt'}, 
 
 {'chunk': ' lived with his wife in an elegant townhouse on Quai Voltaire. He was a likeable man, cultivated of course, 
 with a well-deserved reputation as a generous host and an amusing raconteur.', 
 'source': 'sample1.txt'}, 
 
 {'chunk': 'ous host and an amusing raconteur.', 
 'source': 'sample1.txt'}]

 '''