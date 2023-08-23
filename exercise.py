# Excercise one

def print_1(list_input) -> None:
    """Prints each items of list_input"""
    for item in list_input:
        print(item)

# Exercise two

def print_2(**kwargs) -> None:
    """Prints kwargs with the help of f-strings"""
    pass

# Exercise three

def get_fibonacci_sequence(n):
    """
    Returns the fibonacci sequence up to the n-th item
        - implement functionality
        - add input checks for n or make function more robust
        - add typing
    """
    pass

# Exercise four. Check if number is fibonacci return true or false

def is_fibonacci(number):
    # add typing
    # add input checks
    pass

# Exercise five. Implement Rectangle with two meaningful methods

class Rectangle:
    pass

# Exercise six. Implement Square as you seem fit

class Square:
    pass

# Exercise seven. 

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

# Exercise eight

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
    pass

# Exercise nine

def get_only_item(iterable):
    """
    Returns the first and ONLY value of an iterable
    - implement method
    - comment on why it is difficult to accept all kinds of iterables
    """
    pass

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

if __name__ == "__main__":
    print("\n\nImplement your demos hereafter\n\n")