from random import choice
from string import ascii_uppercase
import logging

logging.basicConfig(level=logging.DEBUG)


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


def path_to_word(path):
    return ''.join([grid[p] for p in path])


def search(path):
    word = path_to_word(path)
    logging.debug('%s: %s' % (path, word))
    if word in dictionary:
        paths.append(path)
    for next_pos in neighbours[path[-1]]:
        if next_pos not in path:
            search(path + [next_pos])
        else:
            logging.debug('skipping %s because in path' % grid[next_pos])


def get_dictionary():
    with open('words.txt') as f:
        return [word.strip().upper() for word in f]


size = X, Y = 2, 2
grid = get_grid()
neighbours = get_neighbours()
dictionary = get_dictionary()

paths = []

for position in grid:
    logging.info('searching %s' % str(position))
    search([position])

print [path_to_word(p) for p in paths]
