from typing import List
import re
import datetime

# Execercise 1
def print_1(list_input) -> None:
    """Prints each items of list_input"""
    for item in list_input:
        print(item.__str__())

# Execercise 2
def print_2(**kwargs) -> None:
    """Prints kwargs with the help of f-strings"""
    key_value_list = []
    for key, value in kwargs.items():
        key_value_list.append(f"{key}={value}")
    text = ', '.join(key_value_list)
    print(text)

# Execercise 3
def get_fibonacci_sequence(n: int) -> List[int]:
    """
    Returns the fibonacci sequence up to the n-th item
        - implement functionality
        - add input checks for n or make function more robust
        - add typing
    """
    first_factor = 0
    second_factor = 1
    result = []
    for index in range(n):
        if index - 1 > 0:
            second_factor = result[index - 1]
        if index - 2 > 0:
            first_factor = result[index - 2]
        if index > 0:
            result.append(first_factor + second_factor)
        else:
            result.append(0)
    return result

# Execercise 4
# check if number is fibonacci return true or false
def is_fibonacci(number: int) -> bool:
    step = 1
    last_item = 0
    while last_item < number:
        sequence = get_fibonacci_sequence(step)
        step = step + 1
        last_item = sequence[-1]
        if sequence.count(number) > 0:
            return True
    return False

# Execercise 5
# Implement Rectangle with two meaningful methods
class Rectangle:
    def __init__(self, height: int = 0, width: int = 0):
        self.height = height
        self.width = width

    def get_area(self) -> int:
        return self.height * self.width

    def get_perimeter(self) -> int:
        return 2 * self.height + 2 * self.width

    def get_highest_edge(self):
        if self.height > self.width:
            return self.height
        else:
            return self.width

    def __str__(self):
        return f"This is a rectangle with with a width {self.width} and {self.height} as height and the area is {self.get_area()}"

# Execercise 6
# implement Square as you seem fit
class Square:
    def __init__(self, edge: int = 0):
        self.edge = edge

    def get_area(self) -> int:
        return self.edge * self.edge

    def get_perimeter(self) -> int:
        return 4 * self.edge

    def __str__(self):
        return f"This is a square with the edge {self.edge} and the area is {self.get_area()}"

# Execercise 7
def split_str(inp: str):
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
    if len(inp) == 0:
        return "Empty string"
    search_result = re.search("^(\d{1,3})(CC|RR)(\d{0,2})$", inp)
    prefix = search_result.group(1)
    base = search_result.group(2)
    if (prefix is None) or (base is None):
        return "outside of scope"
    suffix = search_result.group(3)
    return (prefix, base, suffix)

# Execercise 8
def concat_list_items(*args: List[any]) -> List[str]:
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
    result = args[0]
    
    def get_tree_list(primary_list, secondary_list):
        get_tree_list_result = []
        for primary_list_item in primary_list:
            for secondary_list_item in secondary_list:
                get_tree_list_result.append(f"{primary_list_item}{secondary_list_item}")
        return get_tree_list_result
    for list_index in range(len(args) - 1):
        result = get_tree_list(result, args[list_index + 1])
    return result

# Execercise 9
def get_only_item(iterable):
    """
    Returns the first and ONLY value of an iterable
    - implement method
    - comment on why it is difficult to accept all kinds of iterables
    """
    if len(iterable) > 0:
        return iterable.__getitem__(0)
    else:
        return "It's no an iterable"
        """ It is difficult to accept all kinds of iterables because some iterables, 
        such as generators and lazy iterators, are designed to produce values on-the-fly 
        without necessarily storing all elements in memory. Also some iterables, like lists 
        and dictionaries, are mutable, meaning their contents can be changed after creation. 
        Others, like tuples and strings, are immutable. This difference in mutability affects 
        how these iterables can be manipulated and modified during processing. There are the two
        most importants reasons that I find looking for information in internet """

# Execercise 10
def return_time_db(dt_obj):
    """
    Accepts a datetime object and returns a string representation of it. The
    returned string will be used to store the date and time within a database.
    """
    return dt_obj.strftime('%Y-%m-%d %H:%M:%S')

# Execercise 11
def return_time_wb(dt_obj):
    """
    Accepts a datetime object and returns a string representation of it. The
    returned string will be used to display the date and time on a webpage.
    """
    return dt_obj.strftime('<span> You have visited us on %Y-%m-%d</span>')


if __name__ == "__main__":
    print("\n\nImplement your demos hereafter\n\n")

    # example of simple prints each item of list_input
    print_1(["apple", "banana", "cherry"])

    # example prints kwargs with the help of f-strings
    print_2(flight="A2121", destiny="Germany", city="Berlin", airplane="A350")

    # example fibonacci sequence
    print(get_fibonacci_sequence(30))

    # example is fibonacci checking
    value = 4181
    print(f"is {value} a fibonacci number? answer: {is_fibonacci(4181)}")

    # example Rectangle class
    rectangle = Rectangle(10, 20)
    print(rectangle)

    # example Rectangle class
    square = Square(10)
    print(square)

    print(split_str("111CC1"))

    # example return a list concatenate
    print(concat_list_items([1, 2], ["A", "B"], ["#", "."]))

    print(get_only_item(['ab', 'cd', 'ef']))

    print(return_time_db(datetime.datetime.utcnow()))

    print(return_time_wb(datetime.datetime.utcnow()))
#
# EOF