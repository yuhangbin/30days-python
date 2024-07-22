# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))

it_companies.add('Twitter')

it_companies = it_companies.union({'ABC', 'DEF'})

print(it_companies)

it_companies.remove('ABC')
print(it_companies)

it_companies.discard('ABC')

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.union(B))
print(B.union(A))

print(A.symmetric_difference(B))
del A

age_s = set(age)
print(len(age_s))
print(len(age))

# string is a serial of charactar
# list is modifiable and allow duplicate values
# tuple is unchangable and allow duplicate values
# set is changeable and don't allow duplicate values

words = 'I am a teacher and I love to inspire and teach people.'.split()
swords = set(words)
print(len(swords))
print(swords)

