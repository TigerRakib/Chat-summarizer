import os
import string
import re 
from collections import Counter

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
    print(all_words)
    most_common=Counter(all_words).most_common(top_n)
    return [value for value, _ in most_common]
    
file="example.txt"
print(keyword_analysis(file))