# Day 15: Timing is Everything

from santas_little_helpers import *
import re
from math import lcm

# get all numbers from input, second number is irrelevant because they are all zero
# this is what the input looks like: Disc #1 has 5 positions; at time=0, it is at position 2.

disks = (map(int, re.findall(r'\d+', line)) for line in get_input('inputs/15'))


# in the problem it takes 1 second to get to disc 1, another to get to disc 2, and so on...
# Disc #1 has 5 positions; at time=0, it is at position 4.
# Disc #2 has 2 positions; at time=0, it is at position 1. 
# time:    0 1 2 3 4 5 6 7 ...
# Disc 1:  4 0 1 2 3 4 0 1 2 3 4 ....
# Disc 2:  1 0 1 0 1 0 1 0 1 0 1 0 ...

# so the solution is 5 because after 1 second disk 1 will be at position 0,
# and after one more second, disk 2 will be at position 0

# we can imagine that there is no passage of time when the ball drops - to do that,
# we need to change the initial shift of the disk so we have this:
# time:    0 1 2 3 4 5 6 7 ...
# Disc 1:  0 1 2 3 4 0 1 2 3 4 0 1 2 ...
# Disc 2:  1 0 1 0 1 0 1 0 1 0 1 0 1 ...
# if we do that, we are just looking for the column in which all disks align to zero

# disk_period is the number of holes in the disk
# disk number corresponds to the delay in seconds
# start_pos is the position at time 0 from input

# disks_and_offsets combines the disk period (the number of holes in the disk)
# with the position a disk would have at time zero if the ball would >>instantly<<
# pass through all the disks - we get that by adding disk_no, ie. the delay

# in the above example: 
# disc 1 offset is 4 + 1 = 5 which wraps around to 0
# disc 2 offset is 1 + 2 = 3 which wraps around to 1


disks_and_offsets_pt1 = {disk_period: add_wrap(start_pos, disk_no, disk_period-1)
                                for disk_no, disk_period, _, start_pos in disks}

# part 2, add disk no. 7
disks_and_offsets_pt2 = dict(disks_and_offsets_pt1)
disk_no, disk_period, _, start_pos = map(int, re.findall(r'\d+', 'Disc #7 has 11 positions; at time=0, it is at position 0.'))
disks_and_offsets_pt2[disk_period] = add_wrap(start_pos, disk_no, disk_period-1)


def first_overlap(time_start, period_1, offset_1, period_2, offset_2, in_time_step):
    """ given `time_start` returns the next `time` and `period` for which it holds
    that both `time + offset_1` divided by `period_1` and `time + offset_2` divided by
    `period_2` have no remainders. Such a constelation will be valid for `time`,
    `time + period`, `time + 2 period`, etc. """
    for time in range(time_start, lcm(period_1,period_2)*in_time_step + 1, in_time_step):
        if (time + offset_1) % period_1 == 0 and (time + offset_2) % period_2 == 0:
            return time, lcm(in_time_step, period_2)



def find_overlap_all(in_periods_and_offsets):
    "combines `first_overlap` procedure for a set of periods and offsets (divisors and remainders)"
    # the most important thing with this approach is to have periods and offsets sorted
    # by the offsets
    periods_and_offsets = sorted(in_periods_and_offsets.items(), key=lambda x: x[1])
    # initialize values:
    time = 0
    period = periods_and_offsets[0][0]
    for first, second in zip(periods_and_offsets, periods_and_offsets[1:]):
        time, period = first_overlap(time, *first, *second, period)
    return time




part_1, part_2 = (find_overlap_all(disks_and_offsets) for disks_and_offsets in (disks_and_offsets_pt1, disks_and_offsets_pt2))
print_solutions(part_1, part_2)
# Part 1 solution is: 148737
# Part 2 solution is: 2353212
