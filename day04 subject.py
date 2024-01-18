# subject for day04

# 8.1
e2f = dict(dog='chien', cat='chat', walrus='morse')

# 8.2
print(e2f['walrus'])

# 8.3
f2e = dict(e2f.items())

# 8.4
for i in e2f:
    if e2f[i] == 'chien':
        print(i)
    else:
        pass

# 8.5
print(e2f.keys())

# 8.6
life = {'animals': {'cats': 'Henri', 'octopi': 'Grumpy', 'emus': 'Lucy'},
         'plants': {},
         'other': {}}
# 8.7
print(life.keys())

# 8.8
print(life['animals'].keys())

# 8.9
print(life['animals']['cats'])

# 8.10
squares = {index:pow(value,2) for index, value in enumerate(range(10))}
print(squares)
