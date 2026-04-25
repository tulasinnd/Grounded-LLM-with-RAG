from pathlib import Path

def load_text(file_path: str) -> str: # type hinting
    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    if path.suffix == ".txt":
        return path.read_text(encoding="utf-8")

    else:
        raise ValueError(f"Unsupported file type: {path.suffix}")