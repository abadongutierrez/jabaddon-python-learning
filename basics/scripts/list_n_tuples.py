
# Tuples
# ordered sequence

tuple1 = ("disco", 19, 1.2)
print(type(tuple1))
print(tuple1[0])

# Slicing
print(tuple1[0:2])

print(len(tuple1))

# Tuples are immutable

# Can't sort mixed types - would need to convert to strings first
print(sorted(str(x) for x in tuple1))  # If sorting as strings is desired

# Tuples nesting
tuple2 = (1, 2, ("pop", "rock"), (3, 4), ("disco", 1, (2, 3)))
print(tuple2)

# List
# ordered sequence

list1 = [1, 2, 3.0, "cuatro", "cinco"]
print(list1)
print(list1[-1])
print(list1[2:4])
print(list1[::2])

# List are mutable
list1.extend([11, 12])
print(list1)

print(list1 + [13])

list1.append(13)
print(list1)

list1[-1] = "trece"
print(list1)

del(list1[-1])
del(list1[-1])
print(list1)

del(list1[2])
print(list1)

print("hard rock".split())
print("1, 2, 3, 4, 5".split(", "))

list2 = list1[:] # clone the list
print(list2)

a = [1, 2, 3]
a = set(a)
print(a)