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
[Day 11: Radioisotope Thermoelectric Generators](https://adventofcode.com/2016/day/11) | [Python](python/11.py) | STOP! :hammer: time!! :hourglass_flowing_sand: :hourglass_flowing_sand: OK. So this one was hard. I am very proud of myself for solving this one without looking at any hints, but my part 2 runs for about 10 minutes. I couldn't figure out all of the simplifications one can use to speed things up, most of them are very systematically layed out [in this Reddit post](https://www.reddit.com/r/adventofcode/comments/5hoia9/2016_day_11_solutions/db1v1ws/?utm_source=reddit&utm_medium=web2x&context=3). The only thing I additionally implemented from there was not going back to floor 1 if it is empty. Anyway, I would like to get back to this one at some point, not only to implement all the optimisations, but to clean up my code as well (it is a bit of a mess). But not yet. This is one of my top 2 most exhausting Advent od Code puzzles (looking at you [2020 Day 20 Jurassic Jigsaw Sea Monsters](https://adventofcode.com/2020/day/20)!!!).
[Day 12: Leonardo's Monorail](https://adventofcode.com/2016/day/12) | [Python](python/12.py) | :hammer: :hourglass_flowing_sand: very straightforward, but in that case also very slow implementation (for part 2). I will get back to this one. I would also like to clean up the code a bit as well.
