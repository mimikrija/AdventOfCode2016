# Day 17: Two Steps Forward

from santas_little_helpers import *
from hashlib import md5
from itertools import product

GRID = {complex(x, y) for x, y in product(range(4), repeat=2)}
start = 0+0j
vault = 3_3j

MOVE = {'U':  0-1j,
        'D':  0+1j,
        'L': -1+0j,
        'R':  1+0j,
        }


def paths_from_here(passcode, path):
    "returns possible directions based on md5 hash of `passcode`+`path`"
    seed = passcode + ''.join(c for c in path)
    return [direction for code, direction in zip(md5(seed.encode()).hexdigest()[:4], 'UDLR') if int(code, 16) > 10]


passcode = 'bwnlcvfs'
