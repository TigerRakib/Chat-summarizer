
# 🧠 AI Chat Log Summarizer

**AI Chat Log Summarizer** is a Python-based tool that reads `.txt` chat logs between a user and an AI, analyzes the conversation, and generates a simple, human-readable summary. It includes message statistics and keyword extraction using either basic word frequency or TF-IDF (Term Frequency–Inverse Document Frequency).

---

## 📂 Example Chat Format

```
User: Hello!
AI: Hi! How can I assist you today?
User: Can you explain what machine learning is?
AI: Certainly! Machine learning is a field of AI that allows systems to learn from data.
```

---

## 🚀 Features

-  Parses chat logs formatted with `User:` and `AI:` messages
-  Counts messages per speaker and total exchanges
-  Extracts top 5 most frequently used keywords (excluding stopwords)
-  Optional keyword extraction using **TF-IDF**
-  Batch summarization of multiple `.txt` chat logs in a folder
-  Save summaries in a different folder.

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/TigerRakib/Chat-summarizer.git
   cd Chat-summarizer
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download NLTK stopwords (only once)**
   ```python
   import nltk
   nltk.download('stopwords')
   ```

---

## 🛠️ Usage

### 1. Summarize a Single Chat Log
Edit and run `chat_summarizer.py`:
```python
python chat_summarizer.py
```

### 2. Summarize Multiple Files (Bonus Feature)
Place `.txt` files inside a folder like `chat_logs/`, and call:
```python
summarize_folder("chat_logs", "summaries", use_tfidf=True)
```

---

## 🧪 Sample Summary Output

```
Summaries without using TF-IDF: 
```
![Chat Summarizer Screenshot](https://github.com/TigerRakib/Chat-summarizer/blob/1e953941d3b8e8e449900327d69f78bc40ed3e01/Screenshot%202025-05-20%20150448.png)
![Chat Summarizer Screenshot](https://github.com/TigerRakib/Chat-summarizer/blob/2044a2a7ec9db98d2af6f852ab147793d7d7318a/Screenshot%202025-05-20%20150504.png)
```
Summaries using TF-IDF: 
```
![Chat Summarizer Screenshot](https://github.com/TigerRakib/Chat-summarizer/blob/9c97ba279c8106bc180f9b98fa3d097d80998949/Screenshot%202025-05-23%20004651.png)
![Chat Summarizer Screenshot](https://github.com/TigerRakib/Chat-summarizer/blob/6e6bf87504c256a116e2d9a5d067cf88b54964a7/Screenshot%202025-05-23%20004702.png)
---

## 📁 Project Structure

```
Chat-summarizer/
│
├── chat_summarizer.py         # Main script
├── chat_logs/                 # Folder containing .txt chat files
├── chat_summaries/            # Folder where summaries will be saved
└── README.md                  # Project readme
```

---

## ✅ Requirements

- Python 3.6+
- `nltk`
- `scikit-learn`

---


## ✨ Author

Developed by [Rakib](https://github.com/TigerRakib) — contributions welcome!
