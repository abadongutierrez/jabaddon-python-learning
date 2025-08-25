
import string
# Object and Classes

print(type([1, 2, 3]))
print(type("string"))
print(type((1, 2, 3)))


# Define the class
class Circle(object): 

    # initialize the instace
    # Constructor with default values in params
    def __init__(self, radius = 3, color = 'red'):
        self.radius = radius
        self.color = color

    # like toString in java
    def __str__(self):
        return f"Circle(radius={self.radius}, color={self.color})"
 
    def add_to_radius(self, r):
        self.radius += r


class Rectangle(object):
    # Class attributes (like static)
    default_color = 'blue'

    def __init__(self, height, width, color):
        self.color = color
        self.height = height
        self.width = width

    def area(self):
        return self.length * self.width

    # like toString in java
    def __str__(self):
        return f"Rectangle(height={self.height}, width={self.width}, color={self.color})"
    
# Create instances
red_circle = Circle(5, "red")
print(red_circle)
blue_rectangle = Rectangle(10, 20, "blue")
print(blue_rectangle)
blue_rectangle.color = "orange"
print(blue_rectangle)

# Demonstrate adding a method to the Circle class
red_circle.add_to_radius(2)
print(red_circle)



print(dir(red_circle))

# Press Shift+Enter to run the code.
class TextAnalzer(object):
    
    def __init__ (self, text):
        # remove punctuation
        text = text.replace('.', '')
        text = text.replace('!', '')
        text = text.replace(',', '')
        text = text.replace('?', '')
        self.fmtText = text.lower()


text = TextAnalzer("Hello, World! This is a test.")
print(text.fmtText)

class TextAnalyzer(object):
    
    def __init__(self, text):
        # remove punctuation
        formattedText = text.translate(str.maketrans("", "", string.punctuation))
        
        # make text lowercase
        self.fmtText = formattedText.lower()
        
    def freqAll(self):        
        # split text into words
        words_list = self.fmtText.split()
        
        # Create dictionary
        frequency_dict = {}
        
        # Iterate over the list of words and update the frequency dictionary
        for word in words_list:
            # Use count method for counting the occurrence
            frequency_dict[word] = words_list.count(word)
            
        # Return the frequency dictionary
        return frequency_dict

str = TextAnalyzer("Hello, World! This is a test. A test")
print(str.freqAll())