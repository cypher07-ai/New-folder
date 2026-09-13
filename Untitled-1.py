d = {'eggs': 2, 'milk': 1, 'bread': 3}
d2 = {'apples': 5, 'oranges': 2, 'bananas': 4}
d.update(d2)
print(d)
print(len(d))
print('eggs' in d)
print(list(d.keys()))
print(list(d.values()))
print(d.get('milk'))
print(d.items())
print(d.get('toast'))
d = {'eggs': 2, 'milk': 1, 'bread': 3}
print(d.pop('milk'))
print(d)
a = d.popitem()
print(a)
print(d)
b = str(d)
print(b)
