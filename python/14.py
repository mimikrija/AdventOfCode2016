# Day 14: One-Time Pad

from santas_little_helpers import *
import hashlib

# However, not all of these MD5 hashes are keys, and you need 64 new keys for your one-time pad. A hash is a key only if:

# It contains three of the same character in a row, like 777. Only consider the first such triplet in a hash.
# One of the next 1000 hashes in the stream contains that same character five times in a row, like 77777.

# I think we will need to use some sort of memoization

def has_three_consec_characters(in_string, _):
    for one, two, three in zip(in_string, in_string[1:], in_string[2:]):
        if one == two == three:
            return one
    return False

def has_five_consec_characters(in_string, in_char):
    if not in_char:
        return False
    return any(in_char == one == two == three == four == five for one, two, three, four, five in zip(in_string, in_string[1:], in_string[2:], in_string[3:], in_string[4:]))

in_code = 'ihaygndm'


#@memoize
def generate_hash(start_num, condition, limit=None, character=''):
    number = start_num
    found = False
    while not found:
        number += 1
        candidate = in_code + str(number)
        hash_code = hashlib.md5(candidate.encode()).hexdigest()
        if condition(hash_code, character):
            return number, hash_code, condition(hash_code, character)
        if limit and number > limit:
            return False

    #return number

number = 0
counter = 0
while True:
    number, _, character = generate_hash(number, has_three_consec_characters)
    if generate_hash(number, has_five_consec_characters, number+1000, character):
        counter += 1
        # print(f'{counter}th number is {number}')
    if counter == 64:
        part_1 = number
        break

print_solutions(part_1)
# Part 1 solution is: 15035
