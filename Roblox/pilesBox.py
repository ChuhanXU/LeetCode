import collections

height = collections.Counter(['a', 'b', 'c', 'a', 'b', 'b'])
sortlist = height.values()
print(height)
print(list(sorted(sortlist)))