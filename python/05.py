
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


def generate_password(input_string, is_part_2 = False):
    password = [None for _ in range(8)]
    pos = 0
    start = 0
    while any(char == None for char in password):
        start, fifth_digit, sixth_digit = lowest_positive(start, my_input, 5)
        if not is_part_2:
            password[pos] = fifth_digit
            pos += 1
        else:
            try:
                pos = int(fifth_digit)
                if pos < 8 and password[pos] == None:
                    password[pos] = sixth_digit
            except:
                pass

    return ''.join(char for char in password)


my_input = "uqwqemis"

part_1, part_2 = (generate_password(my_input, is_part_2) for is_part_2 in {False, True})
helpers.print_solutions(part_1, part_2)
# Part 1 solution is: 1a3099aa
# Part 2 solution is: 694190cd
