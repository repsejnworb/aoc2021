import argparse


def tick(fishes):
    spawned = []
    for index, fish in enumerate(fishes):
        if fish == 0:
            fishes[index] = 6
            spawned.append(8)
        else:
            fishes[index] -= 1
    fishes.extend(spawned)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    parser.add_argument("--part2", action="store_true")
    parser.add_argument("--debug", action="store_true")
    parser.add_argument('--days', type=int, default=80)
    args = parser.parse_args()

    with open(f"./{args.inputfile}", 'r') as fio:
        # prepare data
        data = fio.read().strip()
        fishes = [int(x) for x in data.split(',')]

    print(f"Simulating {args.days} days")
    for day in range(1, args.days + 1):
        tick(fishes)

        if args.debug:
            print(fishes)
            print(f"Done simulating {day}, num fishes: {len(fishes)}")
            print()

    print(f"Finished simulation! There are now {len(fishes)}")

    if args.debug:
        import code
        code.interact(local=dict(globals(), **locals()))


if __name__ == "__main__":
    main()
