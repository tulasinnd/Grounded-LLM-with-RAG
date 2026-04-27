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