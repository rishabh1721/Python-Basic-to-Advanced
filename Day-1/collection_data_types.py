# Python has four main collection data types used to store multiple items.

# 1. LIST: Ordered, changeable, allows duplicates. Example: [1, 2, 3]
#    Lists are ideal when you need dynamic data that can be updated.

# 2. TUPLE: Ordered, unchangeable, allows duplicates. Example: (1, 2, 3)
#    Tuples are used for fixed data that should not be modified.

# 3. SET: Unordered, unindexed, no duplicates. Example: {1, 2, 3}
#    Sets are useful for removing duplicates and performing mathematical set operations.

# 4. DICTIONARY: Key-value pairs, ordered (Python 3.7+), changeable, no duplicate keys.
#    Example: {"name": "Rishu", "age": 21}
#    Dictionaries are perfect for structured data with labels.


empty_list = []
my_list = [1,2,3,4,5,6]
print(my_list)
new_list = ['Categories','wall','floor', 'roof', 'ceiling''wall','floor', 'roof', 'ceiling''wall','floor', 'roof', 'ceiling']
print(new_list)

print(my_list[2])
print(my_list[-1])
print(my_list[-2])
print(new_list[0])

header = my_list[0]
data = my_list[1:]
print(header)
print(data)

#get multiple items

print(new_list[:2])       # Prints elements from start up to index 2 (excluded) → first two items.

print(new_list[:])        # Prints the entire list (full slice).

print(new_list[2:])       # Prints elements from index 2 to the end of the list.

print(new_list[1:3])      # Prints elements from index 1 to index 3 (3 excluded).

print(new_list[::2])      # Prints every 2nd element from the entire list (step = 2).

print(new_list[2:6:2])    # Prints elements from index 2 to 6 (6 excluded), taking every 2nd element.

print('wall' in my_list)
print('door' not in my_list)

#functions in list

print(len(my_list))
print(sorted(my_list))
print(sum(my_list))
print(max(my_list))
print(min(my_list))

new_list.append('door')
print(new_list)
new_list.insert(1, 'door')
print(new_list)
new_list += ['door', 'window']
print(new_list)
new_list.remove('door')
print(new_list)
new_list.remove('door')
print(new_list)
new_list.pop()
print(new_list)
new_list.pop()
print(new_list)
new_list.sort()
print(new_list)
new_list.sort(reverse=True)
print(new_list)
new_list.reverse()
print(new_list)
new_list.reverse()
print(new_list)
new_list.reverse()
print(new_list)

new_list.count('wall')
print(new_list)
