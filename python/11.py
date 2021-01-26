# Day 11: Radioisotope Thermoelectric Generators

import itertools
from collections import namedtuple

State = namedtuple('State',['first_floor', 'second_floor', 'third_floor', 'fourth_floor', 'elevator_at'])

# example input
input_state = State(('HM', 'LM'), ('HG',), ('LG',), tuple(), 0)

# my input:
# The first floor contains a polonium generator, a thulium generator, a thulium-compatible microchip, a promethium generator, a ruthenium generator, a ruthenium-compatible microchip,
# a cobalt generator, and a cobalt-compatible microchip.
# The second floor contains a polonium-compatible microchip and a promethium-compatible microchip.
# The third floor contains nothing relevant.
# The fourth floor contains nothing relevant.
# part 1
input_state = State(('PoG', 'TG', 'TM', 'PrG', 'RG', 'RM', 'CG', 'CM') ,('PoM', 'PrM'), tuple(), tuple(), 0)

# part 2
input_state = State(('PoG', 'TG', 'TM', 'PrG', 'RG', 'RM', 'CG', 'CM','EM','EG','DG','DM') ,('PoM', 'PrM'), tuple(), tuple(), 0)


all_generators = {item for floor in input_state[:-1] for item in floor if item[-1]=='G'}
all_microchips = {item for floor in input_state[:-1] for item in floor if item[-1]=='M'}

all_possible_elevators = set(elevator for n in {1,2} for elevator in itertools.combinations(all_generators | all_microchips, n))


def possible_elevator(in_floor, elevator_items):
    return all(item in in_floor for item in elevator_items)

def all_microchips_matched(generators, microchips):
    return all(any(generator[:-1] == microchip[:-1] for generator in generators) for microchip in microchips)

def items_allowed_on_this_floor(in_everything):
    """ checks if `everything` combination is valid for a given floor """
    everything = set(in_everything)
    generators = everything & all_generators
    microchips = everything & all_microchips
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

def elevator_candidates(in_origin, in_destination):
    """ returns list of possible updated states of `origin` and `destination` after taking stuff with elevator"""
    origin = set(in_origin)
    destination = set(in_destination)
    # out_candidates = set()
    # for n in {1,2}:
    #     for elevator in itertools.combinations(origin, n):
    #         out_origin = tuple(sorted(origin - set(elevator)))
    #         out_destination = tuple(sorted(set(elevator) | destination))
    #         if items_allowed_on_this_floor(out_origin) and items_allowed_on_this_floor(out_destination):
    #             out_candidates.add((out_origin, out_destination))
    # return out_candidates
    return set((tuple(sorted(origin - set(elevator))), tuple(sorted(set(elevator) | destination))) for n in {1,2} for elevator in itertools.combinations(origin, n)
                if (items_allowed_on_this_floor(origin - set(elevator))) and
                    items_allowed_on_this_floor(set(elevator) | destination))


def solution_reached(state):
    # all floors are empty except last
    return not any(state[floor] for floor in range(3))


def generate_next_states(in_state):

    in_first_floor, in_second_floor, in_third_floor, in_fourth_floor, elevator_at = in_state

    output_states = set()

    # elevator on first floor
    if elevator_at == 0:
        #go up
        for new_first, new_second in elevator_candidates(in_first_floor, in_second_floor):
            output_states.add(State(new_first, new_second, in_third_floor, in_fourth_floor, elevator_at + 1))
        return output_states

    # elevator on second floor
    if elevator_at == 1:
        # go up
        for new_second, new_third in elevator_candidates(in_second_floor, in_third_floor):
            output_states.add(State(in_first_floor, new_second, new_third, in_fourth_floor, elevator_at + 1))
        # go down, but only if there's still stuff left on first floor to take
        # if not, return so we reduce the number of possible states
        if not in_first_floor:
            return output_states
        for new_second, new_first in elevator_candidates(in_second_floor, in_first_floor):
            output_states.add(State(new_first, new_second, in_third_floor, in_fourth_floor, elevator_at - 1))
        return output_states

    # elevator on third floor
    if elevator_at == 2:
        # go up
        for new_third, new_fourth in elevator_candidates(in_third_floor, in_fourth_floor):
            output_states.add(State(in_first_floor, in_second_floor, new_third, new_fourth, elevator_at + 1))
        # go down
        for new_third, new_second in elevator_candidates(in_third_floor, in_second_floor):
            output_states.add(State(in_first_floor, new_second, new_third, in_fourth_floor, elevator_at - 1))
        return output_states

    # elevator on fourth floor
    if elevator_at == 3:
        # go down
        for new_fourth, new_third in elevator_candidates(in_fourth_floor, in_third_floor):
            output_states.add(State(in_first_floor, in_second_floor, new_third, new_fourth, elevator_at - 1))
        return output_states




def find_first_solution(in_state):
    """ breadth-first solution search. will return the number of steps needed to reach the first solution,
    starting from single initial state `in_state`. """
    solved = False
    states = {in_state}
    visited_states = set(states)

    steps = 0
    while not solved:
        temp_states = set()
        check_start = time.time()
        if any(solution_reached(state) for state in states):
                return steps
        check_end = time.time()
        #print(f'checking time: {check_end-check_start}')
        
        temp_states_start = time.time()
        temp_states = {new_state for state in states for new_state in generate_next_states(state) if new_state not in visited_states}
        temp_states_end = time.time()
        print(f'generating time: {temp_states_end-temp_states_start}')

        visited_states |= temp_states

        steps += 1
        states = temp_states

        print(len(states), len(visited_states))


# print(solution_reached(State(set(), set(), set(), {'HM', 'LM'}, 0)))
import time
start = time.time()
print(find_first_solution(input_state))
end = time.time()
print(end-start)

# 47 part 1
# 71 part 2