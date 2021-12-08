import argparse


def get_efficiency(position, destinations, move_penalty):
    if move_penalty:
        return(666)
    else:
        return sum([abs(position - destination) for destination in destinations])


def brute_force(positions, move_penalty):
    lead = 1000000000
    for position in set(positions):
        efficiency = get_efficiency(position, positions, move_penalty)
        if efficiency < lead:
            lead = efficiency
    return lead


def solve_puzzle(input_data, args):
    def prepare_data(data):
        return [int(x) for x in data.strip().split(',')]
    positions = prepare_data(input_data)
    return brute_force(positions, move_penalty=args.part2)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--test", action="store_true")
    parser.add_argument("--part2", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    input_file = "sample.txt" if args.test else "input.txt"
    with open(f"./{input_file}", 'r') as fio:
        input_data = fio.read()

    answer = solve_puzzle(input_data, args)

    if args.test:
        sample_answer = 168 if args.part2 else 37
        if answer != sample_answer:
            raise AssertionError(f"{answer} is not equal to {sample_answer}")

    print(f"Answer is: {answer}")

if __name__ == "__main__":
    main()
