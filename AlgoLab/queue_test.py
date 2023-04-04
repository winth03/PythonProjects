from stack import ArrayDeque

D = ArrayDeque()
print('Adding last')
for i in range(10):
    D.add_last(i)
    print(i, D._data)

print('Adding first')
for i in range(20, 10, -1):
    D.add_first(i)
    print(i, D._data)

print('Performing the removals')
while not D.is_empty():
    print('Remove first', D.delete_first())
    print('Remove last', D.delete_last())
    print(D._data)