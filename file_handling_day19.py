
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
