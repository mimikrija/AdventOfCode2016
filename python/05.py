
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
    return number, hash_code[5], hash_code[6]


my_input = "uqwqemis"
start = 0
part_1 = ''
part_2 = [None for _ in range(8)]

counter = 0

while any(char == None for char in part_2):
    start, pass_pos, pass_char = lowest_positive(start, my_input, 5)
    try:
        if int(pass_pos) < 8 and part_2[int(pass_pos)] == None:
            part_2[int(pass_pos)] = pass_char
    except:
        continue

print(''.join(c for c in part_2)) # 694190cd

quit()
for _ in range(8):
    start, pass_char, _ = lowest_positive(start, my_input, 5)
    part_1 += str(pass_char)

helpers.print_solutions(part_1)
# Part 1 solution is: 1a3099aa
