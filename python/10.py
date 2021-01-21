# Day 10: Balance Bots

import santas_little_helpers as helpers
import re
from collections import namedtuple, deque

Receiver = namedtuple('Receiver', ['object', 'key'])
Transaction = namedtuple('Transaction', ['giver_key', 'receiver_high', 'receiver_low'])


instructions = helpers.get_input('inputs/10', '\n')

initializations = [list(map(int, re.findall(r'\d+', instruction))) for instruction in instructions if 'value' in instruction]

bot = {}
transactions = deque()

for instruction in instructions:
    # initialize values
    if 'value' in instruction:
        num_1, num_2 = map(int, re.findall(r'\d+', instruction))
        bot[num_2] = bot.get(num_2, []) + [num_1]
    # standard bot transactions
    else:
        giver, receiver_low, receiver_high = re.findall(r'[a-z]+ \d+', instruction)
        giver_key = int(re.findall(r'\d+', giver)[0])
        receiver_low, receiver_low_key = receiver_low.split(' ')
        receiver_high, receiver_high_key = receiver_high.split(' ')
        transaction = Transaction(giver_key, Receiver(receiver_high, int(receiver_high_key)), Receiver(receiver_low, int(receiver_low_key)))
        transactions.append(transaction)

output = {}

while transactions:
    transaction = transactions.pop()
    chips = bot.get(transaction.giver_key, [])
    if len(chips) == 2:
        for receiver, value in zip((transaction.receiver_high, transaction.receiver_low), sorted(chips, reverse=True)):
            if receiver.object == 'bot':
                bot[receiver.key] = bot.get(receiver.key, []) + [value]
            else:
                output[receiver.key] = output.get(receiver.key, []) + [value]
    else:
        transactions.appendleft(transaction)

for key, values in bot.items():
    if 17 in values and 61 in values:
        part_1 = key
        break

part_2 = output[0][0]*output[1][0]*output[2][0]

helpers.print_solutions(part_1, part_2)