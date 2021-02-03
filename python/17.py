# Day 17: Two Steps Forward

from santas_little_helpers import *
from hashlib import md5


def paths_from_here(passcode, path):
    "returns possible directions based on md5 hash of `passcode`+`path`"
    seed = passcode + ''.join(c for c in path)
    return [direction for code, direction in zip(md5(seed.encode()).hexdigest()[:4], 'UDLR') if int(code, 16) > 10]



passcode = 'bwnlcvfs'
