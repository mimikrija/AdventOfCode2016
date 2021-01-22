import itertools

GENERATORS = {'HG', 'LG'}
MICROCHIPS = {'HM', 'LM'}


def all_microchips_matched(generators, microchips):
    return all(any(generator[:-1] == microchip[:-1] for generator in generators) for microchip in microchips)

def items_allowed_on_this_floor(items, floor):
    """ checks whether all `items` in the elevator are compatible with thatever items are in `floor` """
    everything = items | floor
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
    candidates = (combo for n in {1,2} for combo in itertools.combinations(origin, n)
                if (items_allowed_on_this_floor(set(), origin - set(combo))) and
                    items_allowed_on_this_floor(set(combo), destination))
    return candidates

