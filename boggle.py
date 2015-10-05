from random import choice
from string import ascii_uppercase


def get_grid():
    return {(x, y): choice(ascii_uppercase) for x in range(X) for y in range(Y)}


def get_neighbours():
    neighbours = {}

    for position in grid:
        x, y = position
        positions = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1), (x + 1, y),
                     (x + 1, y + 1), (x, y + 1), (x - 1, y + 1), (x - 1, y)]
        neighbours[position] = [p for p in positions if 0 <= p[0] < X and 0 <= p[1] < Y]
    return neighbours


size = X, Y = 2, 2
grid = get_grid()
neighbours = get_neighbours()

paths = []
path = []

for letter1 in grid:
    path.append(letter1)
    paths.append(path[:])

    for letter2 in neighbours[letter1]:
        path.append(letter2)
        paths.append(path[:])

        for letter3 in neighbours[letter2]:
            path.append(letter3)
            paths.append(path[:])

            for letter4 in neighbours[letter3]:
                path.append(letter4)
                paths.append(path[:])
                path.pop()

            path.pop()
        path.pop()
    path.pop()

for path in paths:
    print ''.join([grid[p] for p in path])