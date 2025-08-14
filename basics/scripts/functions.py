
def my_func(v):
    """
    Some documentation about my my_func
    """
    print("Printing inside my_func:", v)

def add1(v):
    """
    Just add 1 to the value
    """
    return v + 1

# python does not allow empty bodies
def no_work():
    pass

def v_print(*v):
    for i in v:
        print(i)

my_func("1")

print(type(my_func("1")))
print(type(add1(1)))
#print(help(add1))

print(type(no_work()))


v_print(1, 2, 3)
v_print([2, 3], 2)
v_print(("3", "4", "%"), [2])

# date in global scope
date = 1982
def fun_scope():
    # date in local scope
    date = 1989
    print(date)
fun_scope()
print(date)

def another_example():
    print(global_val)

# another_example() # fail, variable not defined
global_val = 1
another_example()

