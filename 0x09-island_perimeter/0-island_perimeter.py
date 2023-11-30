#!/usr/bin/python3
""" Island Perimeter """


def island_perimeter(grid):
    """
    Returns  the perimeter described  in grid

    Args:
    grid (List[int]): list of  integers: 0 represents water,
        1 represents land
    """
    visited = set()

    def dfs(i, j):
        """
        Args:
            i (int): row index
            j (int): column index
        """
        if i >= len(grid) or j >= len(grid[0]) or i < 0 or j < 0 or \
                grid[i][j] == 0:
            return 1
        if (i, j) in visited:
            return 0
        visited.add((i, j))
        perim = dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
        return perim
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                return dfs(i, j)
