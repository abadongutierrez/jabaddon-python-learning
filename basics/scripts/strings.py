
string = "Michael Jackson"

print(string[0:4])
print(string[8:12])
# Slice Notation: [start:stop:step]
# ::2 means: start from the beginning, go to the end, but take every 2nd character
print(string[::2])
print(len(string))
print(string + " was a pop start!")
print("*" * 100)

# Strings are immutable!
# string[9] = "m" # TypeError: 'str' object does not support item assignment

print(string.upper())
print(string.replace("Michael", "Janet"))

# format
name = "Rafael"
age = 10000
print("My name is {name}")
print(f"My name is {name}") # notice the f at the begining!
print("My name is {}".format(name))
print("My name is %s and my age %d" % (name, age))

# strings using escape
print("c:\new_path\file.txt")
# Raw strings (no escape)
print(r"c:\new_path\file.txt")
