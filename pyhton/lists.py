my_list = [1, 2, 3, 4]

my_list.append(5)

# you will see the list
print(my_list)
# None, cause append returns nothing
print(my_list.append(6))

list2 = [5, 6, 7]
# Concatenate 2 lists without modifying any of the original lists
print(my_list + list2)