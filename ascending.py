import operator

# Define the dictionary
d = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print('Original dictionary:', d)

# Sort dictionary by value in ascending order
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1))) 
print('Dictionary in ascending order by value:', sorted_d)

# Sort dictionary by value in descending order
sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1), reverse=True))
print('Dictionary in descending order by value:', sorted_d)
