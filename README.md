# Cs-322 PA2

General Notes
• You do not need to validate inputs. You can assume that each input is of the correct type.
• Each exercise includes test cases, but you should also test your code against other test cases.
• These exercises come from Essentials of Programming Languages by Daniel P. Friedman and
Mitchell Wand, 3rd edition, pages 25 to 28 (MIT Press, 2008).
Programming Problems
1. Write a Scheme procedure named invert that takes 1 argument: lst, a list of 2-element lists.
Calling (invert lst) should return a modified copy of lst with each sublist’s elements reversed.

(invert ’())
>()

(invert ’((foo bar)))
>((bar foo))

(invert ’((a 1) (a 2) (1 b) (2 b)))
>((1 a) (2 a) (b 1) (b 2))

Hint: The built-in Scheme procedure list creates a list from the given values. You can use cons
or list to create the lists.

2. Write a Scheme procedure named swapper that takes 3 arguments: two symbols s1 and s2, and a
list of any values slist. Calling (swapper s1 s2 slist) should return a modified copy of slist,
where all occurrences of s1 are replaced by s2 and all occurrences of s2 are replaced by s1.
Importantly, swapper should look inside of sublists to try to do this search-and-replace operation.
Use examples from Chapter 5 of The Little Schemer to guide you.

Examples:
    Input:
    (swapper ’a ’d ’(a b c d))
    Output:
        (d b c a)

    Input:
    (swapper ’a ’d ’(a d () c d))
    Output:
        (d a () c a)

    Input:
    (swapper ’x ’y ’((x) y (z (x))))
    Output:
        ((y) x (z (y)))

3. Write a Scheme procedure named value-count that takes 2 arguments: a symbol s and a list
of any values slist. Calling (value-count s slist) should return the number of times that s
occurs in slist, including in sublists of slist.

(value-count ’x ’((f x) y (((x z) x)))) 
>3

(value-count ’x ’((f x) y (((x z) () x))))
>3

(value-count ’w ’((f x) y (((x z) x))))
>0