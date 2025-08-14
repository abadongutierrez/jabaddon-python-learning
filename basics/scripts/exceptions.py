def my_fun():
    raise ValueError("This is an example error")

try:
    my_fun()
except ValueError as e:
    print(f"ValueError occurred: {str(e)}")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Explanation of try-except blocks for handling exceptions
# The try block lets you test a block of code for errors.
# The except block lets you handle the error.
# You can catch specific exceptions or use a general exception handler.

# Example:
try:
    my_fun()
except ValueError as e:
    print(f"Caught a ValueError: {e}")
except Exception as e:
    print(f"Caught a general exception: {e}")

# Demonstrating multiple except blocks and catching specific exceptions

def divide(a, b):
    return a / b

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Caught a ZeroDivisionError: {e}")
except TypeError as e:
    print(f"Caught a TypeError: {e}")
except Exception as e:
    print(f"Caught a general exception: {e}")
else:
    print(f"Division result is {result}")

# Explain and demonstrate the else clause in try-except
# The else block runs if no exceptions were raised in the try block.

try:
    result = divide(10, 2)
except ZeroDivisionError as e:
    print(f"Caught a ZeroDivisionError: {e}")
except Exception as e:
# Explain and demonstrate the else clause in try-except
# The else block runs if no exceptions were raised in the try block.

try:
    result = divide(10, 2)
except ZeroDivisionError as e:
    print(f"Caught a ZeroDivisionError: {e}")
except Exception as e:
# Show how to create and raise custom exceptions

class CustomError(Exception):
    """Custom exception for specific error cases."""
    pass

def check_value(x):
    if x < 0:
        raise CustomError("Negative value not allowed")

# Discuss best practices for exception handling in Python
# 1. Catch specific exceptions rather than a general Exception.
# 2. Avoid using bare except clauses.
# 3. Use finally for cleanup actions.
# 4. Use else for code that should run if no exceptions occur.
# 5. Raise exceptions with informative messages.
# 6. Create custom exceptions for application-specific errors.
# 7. Log exceptions for debugging and monitoring.
# 8. Keep try blocks small to isolate error-prone code.
try:
    check_value(-1)
except CustomError as e:
    print(f"Caught a custom exception: {e}")
    print(f"Caught a general exception: {e}")
else:
    print(f"Division successful, result is {result}")
# Explain and demonstrate the finally clause in try-except
# The finally block will execute no matter if the try block raises an error or not.

try:
    result = divide(10, 0)
except ZeroDivisionError as e:
    print(f"Caught a ZeroDivisionError: {e}")
except Exception as e:
    print(f"Caught a general exception: {e}")
finally:
    print("This will always execute, cleanup can be done here.")