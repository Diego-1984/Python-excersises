# Excercise one

Example_list =[1,2,3,4]
def print_1(list_input) -> None:
    """Prints each items of list_input"""
    for item in list_input:
        print(item)
print_1(Example_list)

# Exercise two

def print_2(kwargs) -> None:
    """Prints kwargs with the help of f-strings"""
    print(f'I am doing a small test with the languaje {kwargs}.')
   
print_2("Python")

# Exercise three

def get_fibonacci_sequence(n):
    """
    Returns the fibonacci sequence up to the n-th item
        - implement functionality
        - add input checks for n or make function more robust
        - add typing
    """
    if n < 2:
        return n
    else:
        return (n-1) + (n-2)

print(get_fibonacci_sequence(15))

# Exercise four. Check if number is fibonacci return true or false

def is_fibonacci(number):
    if number < 0:
        return False
    a = 0
    b = 1
    while b < number:
        a = b
        b = a + b        
    return b == number

# Examples

print(is_fibonacci(5))
print(is_fibonacci(8))
print(is_fibonacci(9))

# Exercise five. Implement Rectangle with two meaningful methods

class Rectangle:
    def print_rectangle(width, height):
        for i in range(height):
            for j in range(width):
                if i == 0 or i == height - 1 or j == 0 or j == width - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()

# Example
Rectangle.print_rectangle(7, 3)



# Exercise six. Implement Square as you seem fit

class Square:
    def print_square(size):
        for i in range(size):
            for j in range(size):
                if i == 0 or i == size - 1 or j == 0 or j == size - 1:
                    print(" * ", end="")
                else:
                    print("   ", end="")
            print()

# Example
Square.print_square(5)

# Exercise seven. (EXPLICAR HANS)

def split_str(inp):
    """
    Split and return the inputstr as a tuple of three strings. The values to
    be expected for each block are listed hereafter:
        A) Prefix      1-999
        B) Base     CC or RR
        C) Suffix      0-99 (optional)
    Examples:
        "111CC1" -> "111", "CC", "1"
        "3RR" -> "3", "RR", ""
        "CC1" -> outside of scope
        - implement splitting functionality
        - handle cases outside of the scope of this function, see A), B) and C)
        - An empty string is allowed as input:
            - how would you check for an empty string?
            - explain the reasons for your chosen return value
    """
    pass

# Exercise eight (EXPLICAR HANS)

def concat_list_items(*args):
    """
    accepts a variable number of lists (up to 10).
    each list may be empty or has up to 87 elements.
    returns the concatenated elements as a list of strings
    example:
        a = [1, 2]
        b = ["A", "B"]
        c = ["#", "."]
        --> ["1A#", "1A.", "1B#", "1B.", "2A#", "2A.", "2B#", "2B."]
    - implement the general functionality
    - add the check of the input values
    """
    list_A = [1,2]
    list_B = ["A", "B"]
    list_C = ["-", "/"]
    

# Exercise nine

def get_only_item(iterable):

    """
    Returns the first and ONLY value of an iterable
    - implement method
    - comment on why it is difficult to accept all kinds of iterables
    """
    items = list(iterable)
    
    if len(items) != 1:
        return "Iterable must contain exactly one item."
    
    return items[0]

# Example
print(get_only_item("Diego"))

# Some reasons that is dificult to accept all the iterables are memory problems and infinite loops. 
# It´s important to say that numbers are not iterables

   

# Exercise ten

def return_time_db(dt_obj):
    """
    Accepts a datetime object and returns a string representation of it. The
    returned string will be used to store the date and time within a database.
    """

# Exercise eleven

def return_time_wb(dt_obj):
    """
    Accepts a datetime object and returns a string representation of it. The
    returned string will be used to display the date and time on a webpage.
    """

# Exercise twelve

if __name__ == "__main__":
    print("\n\nImplement your demos hereafter\n\n")