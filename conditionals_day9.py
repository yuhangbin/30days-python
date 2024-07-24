
a = 9
if a > 0 :
    print('hello')

if a > 1 :
    print('if')
else :
    print('else')

if a > 0 :
    print('if')
elif a > 10 :
    print('elif')
else:
    print('default')

print('Prefix') if a > 0 else print('A is negative')

if a > 0 or a < 0 :
    print('or')

age = int(input('Enter your age: '))
if age > 18 :
    print('You are a adult.')
else:
    print('You are too young')

my_age = 30
your_age = int(input('Enter your age: '))
diff = 0
older = False
if my_age > your_age :
    diff = my_age - your_age
    older = False
else:
    diff = your_age - my_age
    older = True

print(older)

year = ' year' if diff < 2 else ' years'
if diff > 0 and older:
    print('You are ' + str(diff) + year + ' older than me.')

one = int(input('Enter number one: '))
two = int(input('Enter number two: '))

if one > two :
    print("%d is greater than %d".format(one, two))
elif one == two :
    print(f"{one} is equals {two}")
else:
    print("%d is less than %d" % (one, two))

score = int(input('Check your score:'))
if score >= 80 and score <= 100 :
    print('A')
elif score < 80 and score >=70 :
    print('B')
elif score < 70 and score >= 60 :
    print('C')
elif score < 60 and score >= 50 :
    print('D')
elif score < 50 and score >= 0 :
    print('F')
else:
    print('Unknown')

fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Input fruits:')
if fruit in fruits :
    print('exist')
else:
    fruits.append(fruit)
    print(fruits)


person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

l = len(person['skills'])
if  l > 0 :
    print(person['skills'][l//2])

if l > 0 and 'Python' in person['skills'] :
    print(person['skills'])

if l == 2 and 'JavaScript' in person['skills'] and 'React' in person['skills'] :
    print('Frontend developer')
if person['is_marred'] :
    print('married')
