import argparse
from collections import Counter

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    parser.add_argument("--part2", action="store_true")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument('--days', type=int, default=80)
    args = parser.parse_args()

    with open(f"./{args.inputfile}", 'r') as fio:
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
