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
    if n <= 1:
        return 0

    i = 2
    count = 0

    while i <= n:
        if n % i == 0:
            count += i
            n /= i
        else:
            i += 1

    return count


if __name__ == '__main__':
    n = 4
    print("Min # of operations to reach {} characters: {}"
          .format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} characters: {}"
          .format(n, minOperations(n)))
