import argparse
from collections import Counter

def tick(fishes):
    spawned = []
    for index, fish in enumerate(fishes):
        if fish == 0:
            fishes[index] = 6
            spawned.append(8)
        else:
            fishes[index] -= 1
    fishes.extend(spawned)



""" 
Idea? 
Just count with a list instead. 
Index is the state (0-8), and value is number of fishes in that state.
Then to get a tick update you pop(0) to remove all zeroes and shift
the numbers in one go.
Then add the value that got popped to index(6) and make a new element
of the value at the end of the list (index(8))
"""

def old_solution():
    # setup zeroed counters for each possible state
    fishes = new_counter()

    # handle input
    fishes.update(input_data)

    print(f"Simulating {args.days} days")
    for day in range(1, args.days + 1):
        to_spawn = fishes[0]
        state = new_counter()
        for key, value in fishes.items():
            if key == 0:
                state[6] += value

            state[key] += value

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    parser.add_argument("--part2", action="store_true")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument('--days', type=int, default=80)
    args = parser.parse_args()

    with open(f"./{args.inputfile}", 'r') as fio:
        # prepare data
        input_data = fio.read().strip()
        input_data = [int(x) for x in input_data.split(',')]


    def setup_tracker(input_data):
        states = range(9)
        tracker = Counter(states)
        tracker.subtract(states)
        tracker.update(input_data)
        return [x[1] for x in sorted(tracker.items())]

    tracker = setup_tracker(input_data)

    for day in range(args.days):
        num_finished = tracker.pop(0)
        tracker[6] += num_finished
        tracker.append(num_finished)

    print(f"Number of fishes after {args.days}: {sum(tracker)}")

    if args.debug:
        import code
        code.interact(local=dict(globals(), **locals()))


if __name__ == "__main__":
    main()
