
t = ()
n = ('y1', 'y2', 'y3', 'y4', 'y5')
sis = ('s1', 's2')
bro = ('b1', 'b2')

siblings = sis + bro
print(len(siblings))
f = ('y1',)
m = ('y2',)
print(type(f))
family_members = siblings + f + m
print(family_members)

siblings = family_members[0:len(siblings)]

print(siblings)

parents = family_members[len(siblings):]

print(parents)

fruits = ('apple', 'orange', 'waterlemon')
vegetables = ('tomato', 'potato')
animal = ('pork', 'beef')
food_stuff_tp = fruits + vegetables + animal

food_stuff_lt = list(food_stuff_tp)

print(food_stuff_lt)

mid = food_stuff_tp[len(food_stuff_tp)//2]
print(mid)

print(food_stuff_lt[0:3])
print(food_stuff_lt[-3:])

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries) 
print('Iceland' in nordic_countries)