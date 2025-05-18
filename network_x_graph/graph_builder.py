import networkx as nx
import re
from sentence_transformers import SentenceTransformer
from uuid import uuid4

model = SentenceTransformer('all-MiniLM-L6-v2')

def extract_entities(text):
    return re.findall(r'\b[A-Z][a-z]+(?:\s[A-Z][a-z]+)*\b', text)

def build_graph(texts):
    G = nx.Graph()
    node_embeddings = {}
    for doc in texts:
        entities = extract_entities(doc)
        for entity in entities:
            G.add_node(entity)

        for i in range(len(entities)):
            for j in range(i + 1, len(entities)):
                G.add_edge(entities[i], entities[j])

        doc_id = str(uuid4())
        embedding = model.encode(doc)
        node_embeddings[doc_id] = (embedding, doc)

    return G, node_embeddings

if __name__ == '__main__':
    texts = [
        "This is a sample text.",
        "This is another sample text.",
        "This is yet another sample text.",
    ]
    G, node_embeddings = build_graph(texts)
    print(type(G))
    print(type(node_embeddings))