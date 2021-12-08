import argparse


def get_efficiency(position, destinations, move_penalty):
    if move_penalty:
        def apply_decay(distance):
            return distance * (distance + 1) / 2
        return sum([apply_decay(abs(position - destination)) for destination in destinations])
    else:
        return sum([abs(position - destination) for destination in destinations])


def brute_force(positions, move_penalty):
    lead = 1000000000
    for position in range(max(positions) + 1):
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
    parser.add_argument("--sample", action="store_true")
    parser.add_argument("--part2", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    sample_answer = 168 if args.part2 else 37
    known_answer = 97164301 if args.part2 else 344297

    input_file, expected_answer = ("sample.txt", sample_answer) if args.sample else ("input.txt", known_answer)
    print(f"Running configuration {input_file} expecting answer {expected_answer}")
    with open(f"./{input_file}", 'r') as fio:
        input_data = fio.read()

    answer = solve_puzzle(input_data, args)

    if expected_answer and answer != expected_answer:
        raise AssertionError(f"{answer} is not equal to {expected_answer}")

    print(f"Answer is: {answer}")

if __name__ == "__main__":
    main()
