"""
In the Buddy Strings problem, you need to check if it is possible to get two strings, \
    different from exactly a swap of two letters. \
    If such a swap exists, the program should return True; otherwise, it should return False.\
    The program should also return False if the two strings have different lengths.

Here’s an example of the input and output values of this problem:

Input: s = “ab”, goal = “ba” | Output: True
The output of the above example is true because we can swap the a and b in string s to get the desired goal.
"""


def buddy_strings(s, goal):
    if len(s) != len(goal):
        return False
    if s == goal:
        return len(set(s)) < len(s)
    diffs = [(a, b) for a, b in zip(s, goal) if a != b]
    return len(diffs) == 2 and diffs[0] == diffs[1][::-1]


s = "ab"
goal = "ba"
print(buddy_strings(s, goal))
