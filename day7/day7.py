import argparse


def brute_force(positions):
    lead = 1000000000
    def get_efficiency(position, destinations):
        return sum([abs(position - destination) for destination in destinations])
    for position in set(positions):
        efficiency = get_efficiency(position, positions)
        if efficiency < lead:
            lead = efficiency
    return lead


def solve_puzzle(input_data, args):
    def prepare_data(data):
        return [int(x) for x in data.strip().split(',')]

    positions = prepare_data(input_data)
    return brute_force(positions)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    parser.add_argument("--part2", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    with open(f"./{args.inputfile}", 'r') as fio:
        input_data = fio.read()

    print(f"Answer is: {solve_puzzle(input_data, args)}")

if __name__ == "__main__":
    main()
