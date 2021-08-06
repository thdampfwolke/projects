import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'd': 'D'}

m = collections.ChainMap(a, b)
print(a)
print(b)
print(m)

print('Individual Values')
print(f"a = {m['a']}")
print(f"b = {m['b']}")
print(f"c = {m['c']}")
print(f"c = {m['d']}")

print()
print(f"Keys   = {list(m.keys())}")
print(f"Values = {list(m.values())}")
print()

print('Items:')

for k, v in m.items():
    print('{} = {}'.format(k, v))
print()
print('"d" in m: {}'.format(('d' in m)))
