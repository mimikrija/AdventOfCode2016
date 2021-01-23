import itertools
from collections import namedtuple

State = namedtuple('State',['first_floor', 'second_floor', 'third_floor', 'fourth_floor', 'elevator_at'])

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
    return (set(elevator) for n in {1,2} for elevator in itertools.combinations(origin, n)
                if (items_allowed_on_this_floor(origin - set(elevator))) and
                    items_allowed_on_this_floor(set(elevator) | destination))


def solution_reached(state):
    # all floors are empty except last
    return not any(state[floor] for floor in range(3))


def generate_next_states(in_state):

    in_first_floor, in_second_floor, in_third_floor, in_fourth_floor, elevator_at = in_state
    output_states = []

    # elevator on first floor
    if elevator_at == 0:
        #go up
        for elevator in elevator_candidates(in_first_floor, in_second_floor):
            output_states.append(State(in_first_floor - elevator, in_second_floor | elevator, in_third_floor, in_fourth_floor, elevator_at + 1))
        return output_states

    # elevator on second floor
    if elevator_at == 1:
        # go up
        for elevator in elevator_candidates(in_second_floor, in_third_floor):
            output_states.append(State(in_first_floor, in_second_floor - elevator, in_third_floor | elevator, in_fourth_floor, elevator_at + 1))
        # go down
        for elevator in elevator_candidates(in_second_floor, in_first_floor):
            output_states.append(State(in_first_floor | elevator, in_second_floor - elevator, in_third_floor, in_fourth_floor, elevator_at - 1))
        return output_states

    # elevator on third floor
    if elevator_at == 2:
        # go up
        for elevator in elevator_candidates(in_third_floor, in_fourth_floor):
            output_states.append(State(in_first_floor, in_second_floor, in_third_floor  - elevator, in_fourth_floor | elevator, elevator_at + 1))
        # go down
        for elevator in elevator_candidates(in_third_floor, in_second_floor):
            output_states.append(State(in_first_floor, in_second_floor | elevator, in_third_floor - elevator, in_fourth_floor, elevator_at - 1))
        return output_states

    # elevator on fourth floor
    if elevator_at == 3:
        # go down
        for elevator in elevator_candidates(in_fourth_floor, in_third_floor):
            output_states.append(State(in_first_floor, in_second_floor, in_third_floor | elevator, in_fourth_floor - elevator, elevator_at - 1))
        return output_states




# example input
input_state_example = State({'HM', 'LM'}, {'HG'}, {'LG'}, set(), 0)

# my input:
# The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip,
# a cobalt generator, and a cobalt-compatible microchip.
# The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
# The third floor contains nothing relevant.
# The fourth floor contains nothing relevant.
input_state = State({'PoG', 'TG', 'TM', 'PrG', 'RG', 'RM', 'CG', 'CM'} ,{'PoM', 'PrM'}, set(), set(), 0)




def find_first_solution(in_state):
    """ breadth-first solution search. will return the number of steps needed to reach the first solution,
    starting from single initial state `in_state`. """
    solved = False
    states = [in_state]
    visited_states = states.copy()
    steps = 0
    while not solved:
        temp_states = []
        for state in states:
            if solution_reached(state):
                return steps, state
            else:
                temp_states += [generated_state for generated_state in generate_next_states(state) if generated_state not in visited_states]

        steps += 1
        states = temp_states
        visited_states += temp_states
        # print(len(states), len(temp_states))


# print(solution_reached(State(set(), set(), set(), {'HM', 'LM'}, 0)))

print(find_first_solution(input_state_example))

