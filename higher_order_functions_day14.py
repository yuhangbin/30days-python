
def decorator_with_parameters_1(function) :
    def wrapper(p1, p2, p3):
        print("First {} {} {}".format(p1, p2, p3))
    return wrapper

def decorator_with_parameters(function):
    def wrapper_accepting_parameters(para1, para2, para3):
        function(para1, para2, para3)
        print("I live in {}".format(para3))
    return wrapper_accepting_parameters

@decorator_with_parameters
@decorator_with_parameters_1
def print_full_name(first_name, last_name, country):
    print("I am {} {}. I love to teach.".format(
        first_name, last_name, country))

print_full_name("Asabeneh", "Yetayeh",'Finland')

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland', 'Iceland2']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# map() works for each item in collection
# reduce() sum all items in collection as a result
# filter() reverse all match condition items

# higher order function: takes one or more functions as arguments and returns a function as its result
# closure: inner function that captures and remebers the environment in which it was created. allows data to be attached to the code
# decorators: A decorator is design pattern in Python that allows you to add new functionality to an existing object without modifying its structure.
from collections import defaultdict
from functools import reduce

def is_odd (x):
    return x % 2 == 0
r = list(filter(is_odd, numbers))
print(r)
r = list(map(lambda x: x.upper(), names))
print(r)

print(reduce(lambda x,y: x+y, numbers))

for country in countries :
    print(country)

print(list(map(lambda x : x.upper(), countries)))
print(list(map(lambda x : x*x, numbers)))
print(list(map(lambda x : x.upper(), names)))

print(list(filter(lambda x : 'land' in x, countries)))
print(list(filter(lambda x : len(x) == 6, countries)))
print(list(filter(lambda x : len(x) >= 6, countries)))
print(list(filter(lambda x : x.startswith('E'), countries)))

print(reduce(lambda x,y : x+y, map(lambda x: x*x, filter(lambda x : x > 0, numbers))))

def get_string_lists(l):
    return list(filter(lambda x : isinstance(x, str), l))

print(get_string_lists(countries))

print(reduce(lambda x,y:x+', '+y, countries))

def count_countries_by_letter(countries):
    starting_letter = map(lambda x: x[0], countries)

    def reducer(acc, letter):
        acc[letter] += 1
        return acc
    letter_counts = reduce(reducer, starting_letter, defaultdict(int))

    return dict(letter_counts)

print(count_countries_by_letter(countries))

print(list(filter(lambda x : countries.index(x) < 10, countries)))
print(countries[-10:])

json = [
    {"name": "China", "capital": "Beijing", "population": 1402112000},
    {"name": "Canada", "capital": "Ottawa", "population": 37742154},
    {"name": "Australia", "capital": "Canberra", "population": 25687041},
    {"name": "Argentina", "capital": "Buenos Aires", "population": 45195777},
    {"name": "Brazil", "capital": "Brasília", "population": 212559417},
    {"name": "Belgium", "capital": "Brussels", "population": 11589623},
    {"name": "Chile", "capital": "Santiago", "population": 19116201}
]

print(sorted(json, key=lambda country: country['name']))

json = [
    {"language": "Mandarin Chinese", "speakers": 918000000},
    {"language": "Spanish", "speakers": 460000000},
    {"language": "English", "speakers": 377000000},
    {"language": "Hindi", "speakers": 310000000},
    {"language": "Arabic", "speakers": 310000000},
    {"language": "Portuguese", "speakers": 215000000},
    {"language": "Bengali", "speakers": 230000000},
    {"language": "Russian", "speakers": 154000000},
    {"language": "Japanese", "speakers": 128000000},
    {"language": "Punjabi", "speakers": 125000000}
]
print(sorted(json, key=lambda x : x['speakers'], reverse=True)[:10])

json = [
    {"name": "China", "population": 1402112000},
    {"name": "India", "population": 1366417754},
    {"name": "United States", "population": 331002651},
    {"name": "Indonesia", "population": 273523615},
    {"name": "Pakistan", "population": 220892340},
    {"name": "Brazil", "population": 212559417},
    {"name": "Nigeria", "population": 206139589},
    {"name": "Bangladesh", "population": 164689383},
    {"name": "Russia", "population": 145934462},
    {"name": "Mexico", "population": 128932753},
    {"name": "Japan", "population": 126476461},
    {"name": "Ethiopia", "population": 114963588},
    {"name": "Philippines", "population": 109581078},
    {"name": "Egypt", "population": 102334404},
    {"name": "Vietnam", "population": 97338579},
    {"name": "DR Congo", "population": 89561403},
    {"name": "Turkey", "population": 84339067},
    {"name": "Iran", "population": 83992949},
    {"name": "Germany", "population": 83783942},
    {"name": "Thailand", "population": 69799978}
]

print(sorted(json, key=lambda x : x['population'], reverse=True)[:10])