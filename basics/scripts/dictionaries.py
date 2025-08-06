
# Dictionaries
# Keys and values
# Dictionaries are mutable

dict = {"key1": 1, "key2": 2, "key3": 3}
print(dict)
print(dict["key2"])
dict["key100"] = 100
print(dict)
del(dict["key1"])
print(dict)

print(dict.keys())
print(type(dict.keys())) # list like object, but not a list
print(type(dict.keys()) == type([]))
print(len(dict.keys()))
print(dict.values())
print(type(dict.values()))

print("key100" in dict)
