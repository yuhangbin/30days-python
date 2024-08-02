import re

'''
re.match(): searches only in the beginning of the first line of the string and returns matched objects if found, else returns None.
re.search: Returns a match object if there is one anywhere in the string, including multiline strings.
re.findall: Returns a list containing all matches
re.split: Takes a string, splits it at the match points, returns a list
re.sub: Replaces one or many matches within a string
'''

txt = '''Python is the most beautiful language that a human being has ever created.
I recommend python for a first programming language'''

print(re.search('first', txt, re.I))

print(re.findall('python', txt, re.I))

txt = '''I am teacher and  I love teaching.
There is nothing as rewarding as educating and empowering people.
I found teaching more interesting than any other jobs.
Does this motivate you to be a teacher?'''
print(re.split('\n', txt)) # splitting using \n - end of line symbol

from collections import Counter

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'

words = re.findall(r'\w+', paragraph.lower())

word_counts = Counter(words)

sorted_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

print([(count, word) for word, count in sorted_words])

txt = 'The position of some particles on the horizontal x-axis are -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'

numbers = [int(num) for num in re.findall(r'-?\d+', txt)]

numbers = sorted(numbers)
print(numbers)

max = max(numbers)
min = min(numbers)

print(max - min)

def is_valid_variable(name) :
    if re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*$', name):
        return True
    else:
        return False
    
print(is_valid_variable('1aaa'))
print(is_valid_variable('aaa'))

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''

sentence = re.sub(r'[^a-zA-Z\s]', '', sentence.lower())

print(sentence)

words = sentence.split()

word_counts = Counter(words)
print(word_counts.most_common(3))


