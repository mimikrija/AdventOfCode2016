# Day 7: Internet Protocol Version 7

import santas_little_helpers as helpers
from collections import namedtuple
import re

IP_data = namedtuple('IP_data', ['words', 'hypernet_sequences'])


def is_abba(in_word):
    for first, second, third, fourth in zip(in_word, in_word[1:], in_word[2:], in_word[3:]):
        if first == fourth and second == third and first != second:
            return True
    return False


def is_valid(in_IP):
    if any(is_abba(hypernet_sequence) for hypernet_sequence in in_IP.hypernet_sequences):
        return False
    if any(is_abba(word) for word in in_IP.words):
        return True
    return False


IPs = helpers.get_input('inputs/07', '\n')
all_IPs = []
for line in IPs:
    hypernet_sequences = set(re.findall(r'\[([a-z]+)\]', line))
    only_words = set(re.findall(r'[a-z]+', line)) - hypernet_sequences
    ip = IP_data(only_words, hypernet_sequences)
    all_IPs.append(ip)

part_1 = sum(is_valid(IP) for IP in all_IPs)

helpers.print_solutions(part_1)