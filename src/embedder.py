from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self, model_name):
        self.model = SentenceTransformer(model_name)

    def encode(self, texts):
        return self.model.encode(texts) 
    
'''
Example embeddings: all the chunks are extracted and passed to Embedder and it returns a 384D vector per each chunk

[[-0.06364923  0.03807121  0.04429034 ...  0.09334217  0.02576987   0.00571033]
 [ 0.06989979 -0.03289114  0.03036384 ...  0.11498062  0.00056455  -0.05205606]
 [-0.02193869 -0.04130846  0.00811168 ...  0.0432443  -0.03014704  -0.00684481]
 [-0.05322209  0.030238   -0.08038414 ...  0.05500215 -0.00468529  -0.05101937]
 [-0.06226307 -0.01099838 -0.04059248 ...  0.08809193 -0.00568431   0.02910598]]

A single chunk entry looks like this after adding embedding vector to it
[{'chunk': 'Transformers are powerful models in NLP.\nThey use attention mechanisms.\nRAG combines retrieval with generation.', 
 'source': 'sample.txt', 
 'embedding': array([-6.36492297e-02,  3.80712077e-02,  4.42903377e-02....  2.70334613e-02]]

'''