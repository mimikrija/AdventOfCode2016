# Day 7: Internet Protocol Version 7

import santas_little_helpers as helpers
from collections import namedtuple
import re

IP_data = namedtuple('IP_data', ['words', 'hypernet_sequences'])


def contains_abba(word):
    "checks if `word` contains abba sequence such as 'zuuz' or 'amma' "
    for first, second, third, fourth in zip(word, word[1:], word[2:], word[3:]):
        if first == fourth and second == third and first != second:
            return True
    return False


def bab_from_aba(word_list):
    """generates a set containing 'babs' of all found 'abas' in `word_list`,
    for example: if 'zuz' and 'ama' are found it will return {'uzu', 'mam'}."""
    return {"".join(c for c in [second, first, second]) for word in word_list
                                                        for first, second, third in zip(word, word[1:], word[2:])
                                                        if first == third and first != second}


def is_valid(in_IP, is_part_2=False):
    if not is_part_2:
        # first, eliminate any IPs which have abbas in their hypernet sequence
        if any(contains_abba(hypernet_sequence) for hypernet_sequence in in_IP.hypernet_sequences):
            return False
        # as for the rest, return if any contain abba in their words
        return any(contains_abba(word) for word in in_IP.words)

    if is_part_2:
        # check if any of the words contain bab generated from found abas in hypernet sequences
        return any(bab in word for bab in bab_from_aba(in_IP.hypernet_sequences) for word in in_IP.words)

    return False




IPs = helpers.get_input('inputs/07', '\n')
all_IPs = []
for line in IPs:
    hypernet_sequences = set(re.findall(r'\[([a-z]+)\]', line))
    only_words = set(re.findall(r'[a-z]+', line)) - hypernet_sequences
    ip = IP_data(only_words, hypernet_sequences)
    all_IPs.append(ip)


part_1, part_2 = (sum(is_valid(IP, is_part_2) for IP in all_IPs) for is_part_2 in (False, True))



helpers.print_solutions(part_1, part_2)
# Part 1 solution is: 110
# Part 2 solution is: 242
