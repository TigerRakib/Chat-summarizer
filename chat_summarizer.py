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
    print(user_msgs,ai_msgs,all_msgs)
file="example.txt"
chat_log_parsing(file)