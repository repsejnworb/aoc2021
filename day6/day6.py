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



def new_counter():
    states = range(9)
    counter = Counter(states)
    counter.subtract(states)
    return counter

def create_tracker(range):
    tracker = {}
    for i in range:
        tracker[i] = 0
    return tracker

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


    if args.debug:
        import code
        code.interact(local=dict(globals(), **locals()))


if __name__ == "__main__":
    main()
