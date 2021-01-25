# Day 10: Balance Bots

import santas_little_helpers as helpers
import re
from collections import namedtuple, deque

count_giver_vals = lambda x: len(bot.get(x.giver_key, []))


Receiver = namedtuple('Receiver', ['object', 'key'])
Transaction = namedtuple('Transaction', ['giver_key', 'receiver_high', 'receiver_low'])


instructions = helpers.get_input('inputs/10', '\n')


bot = {}     # this is where all the 'bot' values go to - we use bot number as the key
output = {}  # this is where all the 'output' values go to - we use output number as the key
transactions = deque() # this is a queue of all transactions to be completed

for instruction in instructions:
    # there are two types of instructions:
        # value 5 goes to bot 2 is the 'initialization' type
        # bot 73 gives low to bot 47 and high to bot 68 is the 'standard' type

    # initialization type:
    if 'value' in instruction:
        num_1, num_2 = map(int, re.findall(r'\d+', instruction))
        bot[num_2] = bot.get(num_2, []) + [num_1]

    # standard type:
    else:
        first, second, third = re.findall(r'[a-z]+ \d+', instruction)
        giver_key = int(re.findall(r'\d+', first)[0])
        receiver_low, receiver_low_key = second.split(' ')
        receiver_high, receiver_high_key = third.split(' ')
        # generate a Transaction object and append it to the transaction queue
        transaction = Transaction(giver_key, Receiver(receiver_high, int(receiver_high_key)), Receiver(receiver_low, int(receiver_low_key)))
        transactions.append(transaction)

total_transactions = len(transactions)

transactions = deque(sorted(transactions, key=count_giver_vals))

number_of_steps = 0
while transactions:
    transaction = transactions.pop()
    number_of_steps += 1
    chips = bot.get(transaction.giver_key, [])
    if count_giver_vals(transaction) == 2:
        for receiver, value in zip((transaction.receiver_high, transaction.receiver_low), sorted(chips, reverse=True)):
            # append value to the list of values already present (if no values present, empty list is the default value)
            if receiver.object == 'bot':
                bot[receiver.key] = bot.get(receiver.key, []) + [value]
            else: # receiver is 'output'
                output[receiver.key] = output.get(receiver.key, []) + [value]
    else:
        # this transaction is not solvable yet (at least one value missing), so just put it in the back of the queue
        transactions.appendleft(transaction)

    # "prioritize" the queue based on givers who have most values defined
    transactions = deque(sorted(transactions, key=count_giver_vals))

# but who knows, maybe something to think about?
print(f'number of steps needed was {number_of_steps}, and there were a total of {total_transactions} instructions, excluding initializations.')
# number of steps needed was 2563, and there were a total of 210 instructions, excluding initializations.
# with sort:
# number of steps needed was 210, and there were a total of 210 instructions, excluding initializations.

for bot_num, chips in bot.items():
    if all(num in chips for num in {17, 61}):
        part_1 = bot_num
        break


part_2 = output[0][0]*output[1][0]*output[2][0]

helpers.print_solutions(part_1, part_2)
# Part 1 solution is: 141
# Part 2 solution is: 1209
