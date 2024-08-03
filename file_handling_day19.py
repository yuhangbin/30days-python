
def read_file_and_count(path) :
    with open(path, 'r') as f:
        lines = f.readlines()
        word_count = 0
        print(len(lines))
        for line in lines:
            words = line.split()
            word_count += len(words)
        print(word_count)

read_file_and_count('./txt/obama.txt')
read_file_and_count('./txt/michelle.txt')
read_file_and_count('./txt/donald.txt')

import json
from collections import Counter

def most_spoken_languages(path, topN):
    with open(path, 'r', encoding='utf-8') as f:
        json_txt = json.load(f)
    all_languages = []
    for country in json_txt:
        all_languages.extend(country['languages'])
    language_counter = Counter(all_languages)
    return language_counter.most_common(topN)

print(most_spoken_languages('./json/countries.json', 10))

        
def most_populated_countries(path, topN):
    with open(path, 'r', encoding='utf-8') as f:
        json_txt = json.load(f)
    return sorted(json_txt, key=lambda x : x['population'], reverse=True)[:topN]

print(most_populated_countries('./json/countries.json', 10))

import re

email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
def extract_email(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        txt = f.read()
    return re.findall(email_pattern, txt)

print(extract_email('./data/email_exchanges_big.txt'))
import string

def find_most_common_words(path, topN):
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()
    all_words = re.sub(r"[^a-zA-Z0-9'\s]", '', txt).lower().split()
    word_counter = Counter(all_words)
    return word_counter.most_common(topN)

print(find_most_common_words('./data/donald_speech.txt', 10))


def clean_text(t):
    return re.sub(r'[^\w\s]', '', t.lower())
from data.stop_words import stop_words

def remove_stop_words(t):
    words = t.split()
    return ' '.join([word for word in words if word.lower() not in stop_words])

def get_word_feq(t):
    return Counter(t.split())
import math
def calculate_cosine_similarity(f1, f2):
    words = set(f1.keys()) | set(f2.keys())

    numerator = sum(f1.get(word, 0) * f2.get(word, 0) for word in words)
    s1 = sum(f1.get(word, 0) ** 2 for word in words)
    s2 = sum(f2.get(word, 0) ** 2 for word in words)
    print(s1)
    print(s2)
    print(numerator)
    denominator = math.sqrt(s1) * math.sqrt(s2)

    if not denominator:
        return 0.0
    else:
        return numerator / denominator

def check_text_similarity(text1, text2):
    """Check the similarity between two texts."""
    # Clean and preprocess texts
    text1 = remove_stop_words(clean_text(text1))
    text2 = remove_stop_words(clean_text(text2))
    
    print(len(text1))
    print(len(text2))

    # Get word frequencies
    freq1 = get_word_feq(text1)
    freq2 = get_word_feq(text2)
    
    # Calculate similarity
    similarity = calculate_cosine_similarity(freq1, freq2)
    return similarity

def load_text(file_or_string):
    """Load text from a file or use the provided string."""
    if isinstance(file_or_string, str):
        try:
            with open(file_or_string, 'r') as f:
                return f.read()
        except FileNotFoundError:
            return file_or_string
    else:
        raise ValueError("Input must be a file path or a string.")

# Main application
if __name__ == "__main__":
    # Example usage
    text1 = load_text("data/michelle_speech.txt")
    text2 = load_text("data/melania_speech.txt")
    
    similarity = check_text_similarity(text1, text2)
    print(f"The similarity between the two texts is: {similarity:.2f}")

import csv
def read_csv(path):
    with open(path, 'r') as f:
        csv_reader = csv.reader(f, delimiter=',')
        line_count = 0
        for row in csv_reader:
            line = ' '.join(row).lower()
            if 'python' in line:
                line_count += 1
        print(line_count)

read_csv('./data/hacker_news.csv')
