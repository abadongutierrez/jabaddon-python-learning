# Read the Example1.txt
example1 = "resources/example1.txt"
file1 = open(example1, "r")

print(file1.name)
print(file1.mode)
content = file1.read
print(type(content))

file1.close()
print("File closed:", file1.closed)

# Better way to open a file
with open(example1, "r") as file2:
    print(file2.name)
    print(file2.mode)
    print(file2.read())

print("File closed:", file2.closed)

# Read line by line
with open(example1, "r") as file3:
    for line in file3:
        print(line.strip())

print("Read by chunks:")
# Read by chunks
with open(example1, "r") as file4:
    while True:
        content = file4.read(5) # reads characters
        if not content:
            break
        print("[{}], size: {}".format(content, len(content)))

print("Read lines:")
with open(example1, "r") as file5:
    print(file5.readlines())


# Write line to file
# create directoty tmp
import os
os.makedirs('tmp', exist_ok=True)
example2 = 'tmp/example2.txt'
with open(example2, 'w') as writefile:
    writefile.write("This is line A")

example3 = 'tmp/example3.txt'
with open(example3, 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

example4 = 'tmp/example4.txt'
linesToWrite = ["This is line A\n", "This is line B\n"]
with open(example4, 'w') as writefile:
    writefile.writelines(linesToWrite)

# append to example2
with open(example2, 'a') as writefile:
    writefile.write("\nThis is line B")

# write and read from a file
example5 = 'tmp/example5.txt'
with open(example5, 'a+') as writefile:
    writefile.seek(0, 0) # from beginning
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")
    writefile.seek(0, 0) # from beginning
    print(writefile.read())
