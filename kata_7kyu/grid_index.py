from itertools import chain


def grid_index(grid, indexes):
    flat_grid = list(chain.from_iterable(grid))

    return ''.join([flat_grid[i-1] for i in indexes if i <= len(flat_grid)])
