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
    for line in lines:
        print(line.strip())

file="example.txt"
chat_log_parsing(file)