from src.loader import load_text

def main():
    text = load_text("documents/sample.txt")
    
    print(type(text))
    print(len(text))
    print("Loaded Text: ")
    print(text)

if __name__ == "__main__":
    main()