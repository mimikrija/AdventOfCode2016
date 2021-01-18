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
