import os
from collections import Counter
import socket

# Function to read the file and return the content as a string
def read_file(filepath):
    with open(filepath, 'r') as file:
        return file.read().replace('\n', ' ')

# Function to count total words
def word_count(text):
    return len(text.split())

# Function to find top n words
def top_words(text, top_n=3):
    words = text.split()
    word_counts = Counter(words)
    return word_counts.most_common(top_n)

# Function to handle contractions (for AlwaysRememberUsThisWay.txt)
def handle_contractions(text):
    contractions = {
        "I'm": "I am", "can't": "cannot", "don't": "do not", 
        "I'll": "I will", "you're": "you are",
        "it's": "it is", "we're": "we are", "isn't": "is not",
        "aren't": "are not", "wasn't": "was not", "weren't": "were not",
        "he's": "he is", "she's": "she is", "they're": "they are",
        "I've": "I have", "you'll": "you will", "we'll": "we will",
        "who's": "who is", "wouldn't": "would not", "couldn't": "could not",
        "shouldn't": "should not", "didn't": "did not", "won't": "will not",
        "let's": "let us"
    }
    
    for contraction, replacement in contractions.items():
        text = text.replace(contraction, replacement)
    
    return text

# Paths to the text files inside the container
path_if = '/home/data/IF.txt'
path_always_remember = '/home/data/AlwaysRememberUsThisWay.txt'
output_path = '/home/data/output/result.txt'

# Read the content of the files
text_if = read_file(path_if)
text_remember = read_file(path_always_remember)

# Word counts
count_if = word_count(text_if)
count_remember = word_count(text_remember)
total_count = count_if + count_remember

# Top words and handle contractions
top_3_if = top_words(text_if)
text_remember = handle_contractions(text_remember)
top_3_remember = top_words(text_remember)

# Get the IP address of the container
ip_address = socket.gethostbyname(socket.gethostname())

# Write results to a file
with open(output_path, 'w') as f:
    f.write(f'Total words in IF.txt: {count_if}\n')
    f.write(f'Total words in AlwaysRememberUsThisWay.txt: {count_remember}\n')
    f.write(f'Grand total of words: {total_count}\n')
    f.write(f'Top 3 words in IF.txt: {top_3_if}\n')
    f.write(f'Top 3 words in AlwaysRememberUsThisWay.txt (after handling contractions): {top_3_remember}\n')
    f.write(f'IP address of the container: {ip_address}\n')

# Output the result to the console
with open(output_path, 'r') as result_file:
    print(result_file.read())
