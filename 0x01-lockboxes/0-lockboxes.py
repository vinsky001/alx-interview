#!/usr/bin/python3

"""
Module containing a function `canUnlockAll`
"""


def canUnlockAll(boxes):
    """determines if all the boxes can be opened.

    Args:
        boxes (list):  is a list of lists

    Returns:
        boolean: Return True if all boxes can be opened, else return False
    """
    if not boxes:
        return False
    # Create a set of visited boxes; add 0th element as it is already unlocked
    visited = set([0])
    # Create a list of keys to access different boxes
    keys = boxes[0]
    # Loop through the list of keys and add new keys to keys list
    for key in keys:
        if key not in visited:
            visited.add(key)
            # Add new keys to keys list
            new_keys = [k for k in boxes[key] if k not in visited]
            keys.extend(new_keys)
    return len(visited) == len(boxes)


if __name__ == '__main__':
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))
