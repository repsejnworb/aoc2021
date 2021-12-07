import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    parser.add_argument("--part2", action="store_true")
    args = parser.parse_args()

    with open(f"./{args.inputfile}", 'r') as fio:
        input_lines = fio.read().splitlines()
    print(input_lines)

if __name__ == "__main__":
    main()
