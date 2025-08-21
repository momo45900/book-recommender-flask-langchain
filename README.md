# 📚 Book Recommender Web App

A web application built with **Python Flask** and **LangChain with HuggingFace embeddings** that recommends books based on their descriptions and user queries.  
Users can search for books and view personalized recommendations through an intuitive and visually appealing interface.


---

## 🛠️ Features
- Elegant user interface using **HTML, CSS, and Bootstrap 5**.  
- Book search and recommendations using **FAISS + Sentence Transformers**.  
- Book categorization: Fiction, Children's Fiction, Nonfiction, Children's Nonfiction.  
- Handles book data from CSV files.  
- Saves **vector stores** for faster recommendations.

---

## 🌟 Frontend Skills
- **HTML5 & CSS3**: Structured and clean page layouts using core HTML and CSS.  
- **Bootstrap 5**:  
  - Responsive grid system for book cards and rows.  
  - Ready-to-use classes for buttons, forms, and navigation.  
- **Custom CSS**:  
  - Color and background customization to match the project theme.  
  - Design of book cards with images and titles.  
  - Hover effects and card animations.  
  - Typography enhancements using Google Fonts for better readability.  
- **Responsive Design**: Works well on desktop and mobile devices.  
- **Typography & Aesthetics**: Using fonts like `Lobster` and `Archivo Black` for a professional and stylish look.

---

## 🧰 Backend Skills
- **Python Flask** – Handles server routing, forms, and requests for the web app.  
- **Pandas & NumPy** – Processes and manipulates book CSV data efficiently.  
- **LangChain + HuggingFace Embeddings** – Generates semantic embeddings for smart book recommendations.  
- **FAISS Vector Store** – Caches embeddings for fast similarity search and retrieval.

---

## 📂 Project Structure
```bash
book-recommender/
├── .gitignore
├── README.md
├── requirements.txt
├── app.py
├── tagged_description.txt
├── public/
│ ├── books_with_emotions.csv
│ ├── styles.css
│ ├── cover-not-found.jpg
│ ├── icons8-book-48.png
├── views/
│ └── index.html
└── vector_stores/
```

---

## ⚡ Requirements
- Python 3.10+
- Python packages in `requirements.txt`:
```bash
Flask==2.3.4
pandas==2.1.0
numpy==1.26.0
python-dotenv==1.0.0
faiss-cpu==1.7.4
langchain==0.1.0
sentence-transformers==2.2.2
```


---

## 🚀 Running the Project Locally
1. Clone or download the project to your computer.  
2. Install dependencies:
```bash
pip install -r requirements.txt
python app.py
```
3.Run the Flask app:
```bash
python app.py
```
4.Open your browser and go to:
```bash
http://127.0.0.1:3000
```


