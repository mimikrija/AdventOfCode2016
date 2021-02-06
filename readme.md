# :christmas_tree: :snake: :sparkles: Maja's Advent of Code 2016 :sparkles: :snake: :christmas_tree:

(mostly solved in January 2021)

My goal(s) for this event:

1. improve coding + Python skills :snake:
1. create helpers to use in all future events

## What I learned, what I still don't know

Legend:

:ambulance: - I don't fully understand either the logic or the implementation - HALP!

:hourglass_flowing_sand: - I think this could or should run faster, but I don't know how to optimize it!

:hammer: - Not completely satisfied with solution, but I know how (and plan to) fix it.

Puzzle | Solution(s) | Remarks |
---    |---    |----
[Day 1: No Time for a Taxicab](https://adventofcode.com/2016/day/1) | [Python](python/01.py) | :hammer: 2D grid, Manhattan distance. Might have overcomplicated it, will get back to it...
[Day 2: Bathroom Security](https://adventofcode.com/2016/day/2) | [Python](python/02.py) | :hammer: Again 2D grid. I used complex numbers to define button location on keypads. I guess there must be a way to automate button - coordinate dictionary generation but I was lazy and did it by hand.
[Day 3: Squares With Three Sides](https://adventofcode.com/2016/day/3) | [Python](python/03.py) | Funny twist for part 2 which I solved with a mega list comprehension (so that next time I look at the code I have no idea what I've done).
[Day 4: Security Through Obscurity](https://adventofcode.com/2016/day/4) | [Python](python/04.py) | Used `namedtuple` to better organize room data. I am very satisfied with the double sorting on `Counter` to get the data I need for the first part.
[Day 5: How About a Nice Game of Chess?](https://adventofcode.com/2016/day/5) | [Python](python/05.py) | :hourglass_flowing_sand: Reused my code from [2015 Day 4](https://adventofcode.com/2015/day/4) to get the first part of the logic working. Again, I am curious to know if this thing can run any faster...
[Day 6: Signals and Noise](https://adventofcode.com/2016/day/6) | [Python](python/06.py) | `collections.Counter` for the win again!
[Day 7: Internet Protocol Version 7](https://adventofcode.com/2016/day/7) | [Python](python/07.py) | A more complicated twist on "is password valid" puzzles. I used `namedtuple` to organize IP data, I played around with sets to differentiate between regex groups I used to catch stuff inside brackets and all words. There probably is a regex for that, but I am not that advanced yet.
[Day 8: Two-Factor Authentication](https://adventofcode.com/2016/day/8) | [Python](python/08.py) | :hammer: I started with sets, then had to use lists for the second part. I refused to use `numpy` although that would have probably been a smarter approach. Some code duplication with row/column rotation. Anyway, there's room for improvement here... Oh yes, added a new helper for summation with wrap around which could be used in Day 4!
[Day 9: Explosives in Cyberspace](https://adventofcode.com/2016/day/9) | [Python](python/09.py) | The part that confused me the most was _you'll have to come up with another way to get its decompressed length_ in part 2 puzzle description. It turns out that the second iteration of my part 1 solution (just increasing the length, not actually generating the new string) was enough to solve the problem. The only thing I needed to do was to convert the `while` loop into a recursion and then make sure we decompress everything within `count` range for the second part. I peeked on Reddit though, because my brain froze and I was unable to "translate" the loop approach to the recursion approach on my own.
[Day 10: Balance Bots](https://adventofcode.com/2016/day/10) | [Python](python/10.py) | I tried solving this one using `PriorityQueue`, but that doesn't work because `put()` method seems to be putting items on the right (of course, with respect to priority). So since I'd have a bunch of items with the same priority (number of chips that a giver bot has defined), this would result in an endless loop of continuously `get`ing and `put`ting the same transaction in the queue. I use a combination of a standard queue implementation (`appendleft` to enqueue items which didn't get processed in a given loop) + reverse sorting on the number of chips that a giver bot has defined. This way we end up with a solution which uses the same amount of steps as the number of instructions to get to process all transactions. Not very useful on such a small input set, but noting it here for my future self.
[Day 11: Radioisotope Thermoelectric Generators](https://adventofcode.com/2016/day/11) | [Python](python/11.py) | STOP! :hammer: time!! :hourglass_flowing_sand: :hourglass_flowing_sand: OK. So this one was hard. I am very proud of myself for solving this one without looking at any hints, but my part 2 runs for about 10 minutes. I couldn't figure out all of the simplifications one can use to speed things up, most of them are very systematically layed out [in this Reddit post](https://www.reddit.com/r/adventofcode/comments/5hoia9/2016_day_11_solutions/db1v1ws/?utm_source=reddit&utm_medium=web2x&context=3). The only thing I additionally implemented from there was not going back to floor 1 if it is empty. Anyway, I would like to get back to this one at some point, not only to implement all the optimizations, but to clean up my code as well (it is a bit of a mess). But not yet. This is one of my top 2 most exhausting Advent od Code puzzles (looking at you [2020 Day 20 Jurassic Jigsaw Sea Monsters](https://adventofcode.com/2020/day/20)!!!).
[Day 12: Leonardo's Monorail](https://adventofcode.com/2016/day/12) | [Python](python/12.py) | :hammer: :hourglass_flowing_sand: very straightforward, but in that case also very slow implementation (for part 2). I will get back to this one. I would also like to clean up the code a bit as well.
[Day 13: A Maze of Twisty Little Cubicles](https://adventofcode.com/2016/day/13) | [Python](python/13.py) | My first maze!!! I relied on fantastic [Red Blob Games](https://www.redblobgames.com/pathfinding/a-star/introduction.html) tutorial for BFS and path finding implementations. In second part, I modified the algorithm so as to store the whole frontier as a set, because we needed to count the number of visited coordinates within 50 steps - each frontier ring is one step. I was thinking about putting everything in a single function, but finally opted out for this.
[Day 14: One-Time Pad](https://adventofcode.com/2016/day/14) | [Python](python/14.py) | Another one of those MD5 hash puzzles. I was always trying to find a better way of solving these as my approach was always creating a loop which increments by one, generates hashes, and checks whether the condition is satisfied. In this puzzle, however, we needed to check whether not only a given hash, but also the next 1000 generated hashes satisfies a pair of rules (which are actually compatible). And then in the second part, each hash generation was 2017 consecutive hashes. The key was to just generate a bunch of hashes, and store the ones which satisfy given rules in dictionaries. It is not the most elegant solution because, if a solution isn't found, I need to manually increase the max index of generated hashes, but that too could be automated (I just didn't bother).
[Day 15: Timing is Everything](https://adventofcode.com/2016/day/15) | [Python](python/15.py) | Chinese Remainder Theorem - I used my [2020 Day 13](https://adventofcode.com/2020/day/13) [solution](https://github.com/mimikrija/AdventOfCode2020/blob/main/python/13.py). In order to do so, I needed to change the logic of inputs a bit (at least for it to make sense for me): I imagine that a ball passes through all the disks at once, hence no 1s delay for travelling, and I adjust the starting values accordingly. Then we need to find a moment in time when the initial offset (similar to busses in 2020) + time will overlap with all the other disks' time.
[Day 16: Dragon Checksum](https://adventofcode.com/2016/day/16) | [Python](python/16.py) | Pretty straightforward description. Instead of working on strings, I worked with lists of bools and just converted the final result, which (I think) is faster.
[Day 17: Two Steps Forward](https://adventofcode.com/2016/day/17) | [Python](python/17.py) | A maze (BFS), a 2D grid (complex numbers, yay). Very interesting problem where the state of the maze changes with every step taken. BFS was modified so that we allow visiting positions we already visited before, and the neighbors function returns both the coordinate and the relative position which we use to construct the path. For part 2, we must skip the early exit and let BFS consider all paths and choose the longest one. I loved this puzzle!
[Day 18: Like a Rogue](https://adventofcode.com/2016/day/18) | [Python](python/18.py) | Two things that sped up the solution. 1. there is really no need to generate the whole matrix, because all we need to generate the next row is the state of the previous row. 2. the four "is not safe" conditions actually translate tu non-symmetric configurations of the three characters above the potential character, so it is enough to check if left == right. I think the most time goes on to prepending and appending outer values to each row, I would like to figure out a more elegant solution to that.
[Day 19: Day 19: An Elephant Named Joseph](https://adventofcode.com/2016/day/19) | [Python](python/19.py) | First part was easily solvable by slicing (sushi operator) and shifting the list which contains all the numbers. Basically you keep taking every second element (with possible shifting in a certain case) until the list size is 1. Second part, I couldn't figure out how to do with this sort of slicing. In the meantime I went to Reddit and of course, this puzzle (at least part 1) is a known mathematical problem called [The Josephus Problem](https://www.youtube.com/watch?v=uCsD3ZGzMgE). For second part I wrote a function which removes a single, opposite number per turn which turned out to be way too slow to actually work on my input. So I ran that function for a set of smaller circle sizes and wrote a formula from there. In the meantime I tried linked lists, doubly linked lists (implemented using dictionaries), but all of the approaches were way to slow.
[Day 20: Firewall Rules](https://adventofcode.com/2016/day/20) | [Python](python/20.py) | I naively thought that I should just create sets of ranges in the input and do some set manipulation to find solutions to both parts of the puzzles. But, for such a huge amount of numbers, this made no sense - the range of all possible numbers goes from 0 to 4294967295, whereas we end up (in my case) with only 117 allowed numbers. The key was to sort the forbidden ranges by the lower number and then loop through them. If a number is in a forbidden range, the next number to check is the upper limit of that range + 1. I've used the same logic repeatedly to find all the allowed numbers (ie. to count them) - but was stuck with a series of off-by one errors in both directions.
[Day 21: Scrambled Letters and Hash](https://adventofcode.com/2016/day/21) | [Python](python/21.py) | :hammer: First part was relatively easy, but long: carefully implementing a list of string manipulation rules. For the second part I got stuck because I couldn't figure out how to unscramble (I tried running the instructions in reverse order with arguments flipped, but that would work only for some instructions - I think the most difficult instruction to reverse is the "rotate based on position"). I went to Reddit to look for clues - it literally never came to my mind to simply try out scrambling all permutations of the part 2 input string until I find it. Ah.. Anyway, I would still like to figure out a less brute-force (although this was relatively fast) way of solving this puzzle.
[Day 22: Day 22: Grid Computing](https://adventofcode.com/2016/day/22) | [Python](python/22.py) | Interesting puzzle, but it works because of many assumptions (the wall is not in the top row). I used BFS again. Not to happy about the whole experience. I had to peek on Reddit to figure out the x5 for the second part (if we want to move a specific tile to the side, we need to shift everything around 5 times). Meh.
[Day 23: Safe Cracking](https://adventofcode.com/2016/day/23) | [Python](python/23.py) | I don't think I would figure out part two without looking at hints. I partially figured it out, partially not. Overall I'm not good at these mathematical induction types of puzzles...
