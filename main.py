import openai
import faiss
import numpy as np
import os

# Set your OpenAI API key

openai.api_key = os.getenv("OPENAI_API_KEY")
# Load documents
with open("documents.txt", "r") as f:
    docs = [line.strip() for line in f.readlines() if line.strip()]

# Function to get embedding from OpenAI API
def get_embedding(text):
    response = openai.Embedding.create(
        model="text-embedding-ada-002",
        input=text
    )
    return response['data'][0]['embedding']

# Generate and index document embeddings
print("Generating embeddings...")
doc_embeddings = [get_embedding(doc) for doc in docs]
doc_embeddings = np.array(doc_embeddings).astype("float32")

index = faiss.IndexFlatL2(len(doc_embeddings[0]))
index.add(doc_embeddings)

# Main QA function
def answer_question(query):
    query_vector = np.array([get_embedding(query)]).astype("float32")
    D, I = index.search(query_vector, k=2)
    context = "\n".join([docs[i] for i in I[0]])

    prompt = f"""You are an assistant helping users based on the following context.

Context:
{context}

Question: {query}
Answer:"""

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

# Run interactive loop
while True:
    user_q = input("\nAsk a question (or type 'exit'): ")
    if user_q.strip().lower() == "exit":
        break
    try:
        print("\nAnswer:", answer_question(user_q))
    except Exception as e:
        print("Error:", e)
