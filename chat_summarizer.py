import os
import string
import re 
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords as nltk_stopwords
import nltk

nltk.download('stopwords')

stopwords = set([
    'the', 'is', 'and', 'a', 'an', 'can', 'you', 'for', 'to', 'of', 'in', 'it', 'its', 'this', 'that', 'on', 'with'
])
def chat_log_parsing(file_path):
    with open(file_path,'r') as file:
        lines= file.readlines()
    user_msgs=[]
    ai_msgs=[]
    all_msgs=[]
    for line in lines:
        if line.startswith("User:"):
            msg = line[len("User:"):].strip()
            user_msgs.append(msg)
            all_msgs.append(msg)
        elif line.startswith("AI:"):
            msg = line[len("AI:"):].strip()
            ai_msgs.append(msg)
            all_msgs.append(msg)
    return user_msgs,ai_msgs,all_msgs

def clean_msgs(msg):
    msg=msg.lower()
    msg = re.sub(r"[^\w\s]", '', msg)
    return msg
def message_statistics(filename):
    user_msgs,ai_msgs,all_msgs=chat_log_parsing(filename)
    total_msgs=len(all_msgs)
    count_user_msgs=len(user_msgs)
    count_ai_msgs=len(ai_msgs)
    return total_msgs,count_user_msgs,count_ai_msgs

def keyword_analysis(file,top_n=5):
    user,ai,all_msgs=chat_log_parsing(file)
    all_words=[]
    for msg in all_msgs:
        words=clean_msgs(msg).split()
        for word in words:
            if word not in stopwords:
                all_words.append(word)
    #print(all_words)
    most_common=Counter(all_words).most_common(top_n)
    return [value for value, _ in most_common]

def tfidf_analysis(file, top_n=5):
    user,ai,all_msgs=chat_log_parsing(file)
    default_stopwords = set(nltk_stopwords.words('english'))
    custom_stopwords = default_stopwords.union({'hello', 'hi', 'thanks', 'please', 'okay', 'yes', 'no'})
    vectorizer = TfidfVectorizer()
    tfidf_mat = vectorizer.fit_transform(all_msgs)
    scores = tfidf_mat.sum(axis=0).A1
    voca = vectorizer.get_feature_names_out()
    keywords_scores = list(zip(voca, scores))
    filtered_keywords = [(word, score) for word, score in keywords_scores if word.lower() not in custom_stopwords]
    sorted_keywords = sorted(filtered_keywords, key=lambda x: x[1], reverse=True)
    return [val for val, _ in sorted_keywords[:top_n]]

def generate_summary(filename,use_idf=True):
    user,ai,all_msgs=chat_log_parsing(filename)
    total=len(user)+len(ai)
    if use_idf:
        keywords=tfidf_analysis(filename)
    else:
        keywords=keyword_analysis(filename)
    summary = f"""Summary for {filename}:
- The conversation had {total} exchanges.
- The user asked mainly about {' '.join(keywords[:2])} and its uses.
- Most common keywords: {', '.join(keywords)}
    """
    return summary
file="example.txt"
print(generate_summary(file))