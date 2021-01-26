# Day 13: A Maze of Twisty Little Cubicles

my_input = 1358
my_input = 10 # example


def is_open(in_coordinate):
    x, y = in_coordinate
    ones = bin(x*x + 3*x + 2*x*y + y + y*y + my_input).count('1')
    return ones % 2 == 0


# What is the fewest number of steps required for you to reach 31,39? (starting from 1,1)
goal = (31, 39)
goal = (7, 4) # example
