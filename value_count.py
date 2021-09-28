'''
Developed by Shane Flynn
Part 1
This Python program must be saved in a file named value_count.py. It must include the following parts.

A function named value_count that accepts 2 arguments: a value (of any type) and a list. This function returns the number of times that the value occurs inside the list.
Do not use Python's built-in count() function to implement value_count! If you do, I will give you exactly 2 points for this part.
Your value_count function does not need to look inside of nested objects (e.g., lists inside other lists) to search for occurrences of the value.
A main program that calls the value_count function with the following arguments.
1 and the list [4, 3, 2, 1]
1 and the list [1, 2, 3, 1, 2, 2]
2 and the list [1, 2, 3, 1, 2, 2]

The main program must print the following output, formatted in the following way. Where you see $OUTPUT, substitute the output from the given function call.
value_count test 1:
$OUTPUT

value_count test 2:
$OUTPUT

value_count test 3:
$OUTPUT
'''

def value_count(value, list):
    count = 0
    for i in list:
        if i == value:
            count += 1
    return count

if __name__ == "__main__":
    print("value_count test 1:\n%i" % value_count(1, [4, 3, 2, 1]))
    print("value_count test 2:\n%i" % value_count(1, [1, 2, 3, 1, 2, 2]))
    print("value_count test 3:\n%i" % value_count(2, [1, 2, 3, 1, 2, 2]))