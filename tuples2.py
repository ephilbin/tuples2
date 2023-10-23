d = {'foo': 1, 'bar': 2, 'baz':3, 'bad': 4} #dictionary with three tuples
while len(d) > 3: 
    print(d.popitem()) 
print('Done.')