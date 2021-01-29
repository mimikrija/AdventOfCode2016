# Day 14: One-Time Pad

from santas_little_helpers import *
import hashlib


def has_three_consec_characters(in_string):
    for one, two, three in zip(in_string, in_string[1:], in_string[2:]):
        if one == two == three:
            return in_string, one
    return False, False


def has_five_consec_characters(in_string):
    return any(one == two == three == four == five for one, two, three, four, five in zip(in_string, in_string[1:], in_string[2:], in_string[3:], in_string[4:]))


def generate_hash(index, in_code, is_part_2=False):
    seed = in_code + str(index)
    hash_code = hashlib.md5(seed.encode()).hexdigest()
    if not is_part_2:
        return hash_code
    else:
        for _ in range(2016):
            hash_code = hashlib.md5(hash_code.encode()).hexdigest()
        return hash_code


def generate_hash_dicts(max_num, in_code, is_part_2=False):
    hashes = (generate_hash(index, in_code, is_part_2) for index in range(max_num))
    threes = {n: (hash_code, character) for n, (hash_code, character) in enumerate(has_three_consec_characters(hash_code) for hash_code in hashes) if character}
    fives = {n: hash_code for n, (hash_code, character) in threes.items() if has_five_consec_characters(hash_code)}
    return threes, fives


def has_fives_in_next_1000(index, _, character, fives):
    return any(5*character in fives.get(check,'') for check in range(index+1, index+1002))


def find_first_64(max_num, in_code, is_part_2=False):
    threes, fives = generate_hash_dicts(max_num, in_code, is_part_2)
    count = 0
    for index, three in threes.items():
        count += has_fives_in_next_1000(index, *three, fives)
        if count == 64:
            return index



in_code = 'ihaygndm'

# the first argument is the max number of hashes to generate 
# I just played around with it until I got a solution
part_1 = find_first_64(16000, in_code)
part_2 = find_first_64(25000, in_code, True)

print_solutions(part_1, part_2)
# Part 1 solution is: 15035      ~ 0.4 s
# Part 2 solution is: 19968      ~ 52 s
