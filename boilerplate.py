import argparse

def solve_puzzle(input_data, args):
    return "Not solved"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    parser.add_argument("--part2", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    with open(f"./{args.inputfile}", 'r') as fio:
        input_data = fio.read()

    print(solve_puzzle(input_data, args))

    if args.debug:
        import code
        code.interact(local=dict(globals(), **locals()))

if __name__ == "__main__":
    main()
