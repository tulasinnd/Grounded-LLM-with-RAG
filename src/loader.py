from pathlib import Path

def load_documents(folder_path: str):
    documents = []

    folder = Path(folder_path)

    for file in folder.glob("*"):
        if file.suffix == ".txt":
            text = file.read_text(encoding="utf-8")

            documents.append({
                "source": file.name,
                "text": text
            })

    return documents

'''
Example documents:

[{'source': 'sample.txt', 'text': 'Transformers are powerful models in NLP.\nThey use attention mechanisms.
\nRAG combines retrieval with generation.'}, 

{'source': 'sample1.txt', 'text': '"You don\'t have to be French to enjoy a decent red wine," Charles Jousselin
de Gruse used to tell his foreign guests whenever he entertained them in Paris. "But you do have to be French to
recognize one," he would add with a laugh.\n\nAfter a lifetime in the French diplomatic corps, the Count de 
Gruse lived with his wife in an elegant townhouse on Quai Voltaire. He was a likeable man, cultivated of course,
with a well-deserved reputation as a generous host and an amusing raconteur.'}]

'''