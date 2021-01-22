import itertools

GENERATORS = {'HG', 'LG'}
MICROCHIPS = {'HM', 'LM'}


def all_microchips_matched(generators, microchips):
    return all(any(generator[:-1] == microchip[:-1] for generator in generators) for microchip in microchips)

def items_allowed_on_this_floor(everything):
    """ checks if `everything` combination is valid for a given floor """
    generators = everything & GENERATORS
    microchips = everything & MICROCHIPS
    # there are no generators, it is ok
    if not generators:
        return True
    # there are no microchips so nothing to fry, it is ok
    if not microchips:
        return True
    # there are both groups present, we need to check if any of the microchips something will be fried
    # if there are more microchips than generators, some microchips will be fried because there is no way
    # a matching generator exists
    if len(microchips) > len(generators):
        return False
    return all_microchips_matched(generators, microchips)

def elevator_candidates(origin, destination):
    """ returns all elevator candidates (1, and 2 - tuples) which won't mess anything
    up on either `origin` or `destination`"""
    return (combo for n in {1,2} for combo in itertools.combinations(origin, n)
                if (items_allowed_on_this_floor(origin - set(combo))) and
                    items_allowed_on_this_floor(set(combo) | destination))

# example input
input_state = [
    ['HM', 'LM'],   # floor 1
    ['HG'],         # floor 2
    ['LG'],         # floor 3
    [],             # floor 4
]

def solution_reached(state):
    # all floors are empty except last
    return not any(state[floor] != [] for floor in range(3))
