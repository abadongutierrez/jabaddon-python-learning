
def reverse_string(text):
    """
    Reverse a string using Python's slice notation.
    
    Args:
        text (str): The string to reverse
        
    Returns:
        str: The reversed string
    """
    return text[::-1]


def main():
    """Main function to demonstrate string reversal."""
    string = "Hello Python!"
    reversed_string = reverse_string(string)
    
    print(f"Original: {string}")
    print(f"Reversed: {reversed_string}")


if __name__ == "__main__":
    main()

