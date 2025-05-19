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

def keyword_analysis(all_msgs,top_n=5):
    all_words=[]
    for msg in all_msgs:
        words=clean_msgs(msg).split()
        for word in words:
            if word not in stopwords:
                all_words.append(word)
    #print(all_words)
    most_common=Counter(all_words).most_common(top_n)
    return [value for value, _ in most_common]

def tfidf_analysis(all_msgs, top_n=5):
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

def generate_summary(filename,user,ai,all_msgs,use_idf=True):
    total=len(user)+len(ai)
    if use_idf:
        keywords=tfidf_analysis(all_msgs)
    else:
        keywords=keyword_analysis(all_msgs)
    summary = f"""{filename}:
- The conversation had {total} exchanges.
- The user asked mainly about {' '.join(keywords[:2])} and its uses.
- Most common keywords: {', '.join(keywords)}
    """
    return summary

def summarize_folder(input_path,output_path,use_tfidf=False):

    for filename in os.listdir(input_path):
        if filename.endswith(".txt"):
            filepath = os.path.join(input_path, filename)
            user_msgs, ai_msgs, all_msgs = chat_log_parsing(filepath)
            summary = generate_summary(filepath, user_msgs, ai_msgs, all_msgs, use_tfidf)
            print(f"Summary: {summary}")


if __name__ == "__main__":
    chat_log_folder="chat_logs"
    output_folder="chat_summaries"
    summarize_folder(chat_log_folder, output_folder, use_tfidf=False)
