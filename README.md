
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
Summary: chat_logs\example.txt:
- The conversation had 4 exchanges.
- The user asked mainly about machine learning and its uses.
- Most common keywords: machine, learning, hello, hi, how
```

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
