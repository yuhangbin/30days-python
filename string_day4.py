r = 'Three' + ' two one'
print(r)
print(r.upper())
print(r.lower())
print(r.swapcase())
print(r[1:])
print(r.find('one'))
print(r.index('one'))
print(r.replace('one', 'zero'))
print(r.split(' '))
print(r[10])
arr = r.split(' ')
print(''.join(a[0].upper() for a in arr))
print(r.find('T'))
print(r.rfind('o'))
print(r.find('One'))
print(r[r.find('two'):len(r)])
print(r.startswith('The'))
print(r.endswith('one'))
print(r.replace(' ', ''))
arr=['1', '2']
print('#'.join(arr))
print('1\n2')
print('1\t2\n3')
a=1
b=2
print(f'{a}+{b} = {a+b}')