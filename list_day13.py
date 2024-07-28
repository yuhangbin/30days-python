
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

arr = [i for i in numbers if i <= 0]

print(arr)

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]


flattened_list = [item for sublist in list_of_lists for subsublist in sublist for item in subsublist]

print(flattened_list)

result = [(i, 1, i, i**2, i**3, i**4, i**5) for i in range(11)]

print(result)

countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

result = [
    [c.upper(), c[:3].upper(), capital.upper()]
    for [c, capital] in [item[0] for item in countries]
]

print(result)

result = [
    [{'country': c.upper(), 'city': capital.upper()}]
    for [c, capital] in [ item[0] for item in countries]
]

print(result)

names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]

result = [
    [t[0] + ' ' + t[1]]
    for t in [item[0] for item in countries]
]
print(result)

s_func = lambda x1, y1, x2, y2 : (x1 - x2) / (y1 - y2)

print(s_func(1, 1, 2,2))
