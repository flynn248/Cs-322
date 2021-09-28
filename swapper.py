'''
Developed by Shane Flynn

Part 2
This Python program must be saved in a file named swapper.py. It must include the following parts.

A function named swapper that accepts 3 arguments: two values s1 and s2 (of any type) and a list. This function returns a new list that contains the same values as the 
original list, except all occurrences of s1 are replaced by s2 and all occurrences of s2 are replaced by s1 in the new list.

A main program that calls the swapper function with the following arguments.
4, 6, and the list [4, 3, 2, 1]
3, "blue", and the list ["red", "green", "blue", "purple"]
1, 2, and the list [1, 2, 3, 1, 2, 2]

The main program must print the following output, formatted in the following way. Where you see $OUTPUT, substitute the output from the given function call.
swapper test 1:
$OUTPUT

swapper test 2:
$OUTPUT

swapper test 3:
$OUTPUT
'''

def swapper(s1, s2, list):
    i = 0
    for value in list:
        if s1 == value:
            list[i] = s2
        elif s2 == value:
            list[i] = s1
        i += 1

    return list

if __name__ == "__main__":
    print("swapper test 1:\n%s" % swapper(4, 6, [4, 3, 2, 1]))
    print("swapper test 2:\n%s" % swapper(3, "blue", ["red", "green", "blue", "purple"]))
    print("swapper test 3:\n%s" % swapper(1, 2, [1, 2, 3, 1, 2, 2]))