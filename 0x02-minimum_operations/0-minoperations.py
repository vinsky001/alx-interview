#!/usr/bin/python3
"""
In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that
calculates the fewest number of operations needed to result in
exactly n H characters in the file.

- Prototype: def minOperations(n)
- Return an integer
- If n is impossibl to achieve, return 0
"""


def minOperations(n):
    """clculates the fewest number of operations needed to
    result in exactly n H characters in the file."""
    operations = 0
    chars = 'h'
    buffer = ''
    while len(chars) < n:
        if n % len(chars) == 0:
            buffer = chars
            operations += 1
        chars += buffer
        operations += 1
    return operations
