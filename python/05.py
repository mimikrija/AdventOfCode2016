
import santas_little_helpers as helpers
import hashlib

has_n_leading_zeroes = lambda code, n: all(c == '0' for c in code[:n])

def lowest_positive(start_num, in_code, leading_zeroes):
    number = start_num
    found = False
    while not found:
        number += 1
        candidate = in_code + str(number)
        hash_code = hashlib.md5(candidate.encode()).hexdigest()
        found = has_n_leading_zeroes(hash_code, leading_zeroes)
    return number, hash_code[5]


my_input = "uqwqemis"
start = 0
part_1 = ''
for _ in range(8):
    start, pass_char = lowest_positive(start, my_input, 5)
    part_1 += str(pass_char)

helpers.print_solutions(part_1)
# Part 1 solution is: 1a3099aa
