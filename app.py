from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
import pickle
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

load_dotenv()


books = pd.read_csv("public/books_with_emotions.csv")

def save_vector_store(vector_store, filename):
    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    with open(f"{filename}.pkl", "wb") as f:
        pickle.dump(vector_store, f)

def load_vector_store(filename):
    with open(f"{filename}.pkl", "rb") as f:
        return pickle.load(f)

def context_extractor(filename, user_query, top_k=16):
    pkl_path = f"{filename}.pkl"

    if os.path.exists(pkl_path):
        vector_store = load_vector_store(filename)
    else:
        with open("tagged_description.txt", "w", encoding="utf-8") as f:
            for desc in books["tagged_description"]:
                f.write(desc.strip() + "\n=\n")

        raw_docs = TextLoader("tagged_description.txt", encoding="utf-8").load()
        text_splitter = CharacterTextSplitter(chunk_size=10000, chunk_overlap=0, separator="=")
        docs = text_splitter.split_documents(raw_docs)

        embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vector_store = FAISS.from_documents(docs, embedder)

        save_vector_store(vector_store, filename)

    recs = vector_store.similarity_search_with_score(user_query, k=top_k)

    
    recs.sort(key=lambda x: x[1], reverse=True)

    
    books_list = []
    for doc, score in recs:
        try:
            book_id = int(doc.page_content.strip('"').split()[0])
            books_list.append(book_id)
        except:
            continue

    book_recs = books.loc[
        books["isbn13"].isin(books_list),
        ["title", "large_thumbnail"]
    ].to_dict(orient="records")

    return book_recs

app = Flask(__name__, static_folder="public", template_folder="views")

@app.route("/")
def index():
   
    books["large_thumbnail"] = books["thumbnail"].astype(str) + "&fife=w800"
    books["large_thumbnail"] = np.where(
        books["thumbnail"].isna(),
        "public/cover-not-found.jpg",
        books["large_thumbnail"],
    )

   
    categories = [
        ("Fiction", "Fiction"),
        ("Children's Fiction", "Children's Fiction"),
        ("Nonfiction", "Nonfiction"),
        ("Children's Nonfiction", "Children's Nonfiction"),
    ]

    book_data = []
    for cat_key, cat_name in categories:
        cat_books = books.loc[
            books["simple_categories"] == cat_key,
            ["title", "large_thumbnail"]
        ].head(4).to_dict(orient="records")

        book_data.append({
            "category": cat_name,
            "books": cat_books
        })

    return render_template("index.html", categories=book_data)

@app.route("/submit", methods=["POST"])
def submit():
    user_query = request.form.get("query", "")
    rec = context_extractor("books", user_query, top_k=16)
    return render_template("index.html", books_rec=rec)

if __name__ == "__main__":
    app.run(port=3000, debug=True)