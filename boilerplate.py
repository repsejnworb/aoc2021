import argparse
from enum import Enum

class Answers(Enum):
    SAMPLE_PART1 = "BOILERPLATE"
    SAMPLE_PART2 = "BOILERPLATE"
    SOLVED_PART1 = None
    SOLVED_PART2 = None


def solve_puzzle(data, part2=False):
    def prepare_data():
        return data

    def solve_puzzle():
        return "BOILERPLATE"

    data = prepare_data()
    answer = solve_puzzle()
    return answer


def BOILERPLATE():
    parser = argparse.ArgumentParser()
    parser.add_argument("--sample", action="store_true")
    parser.add_argument("--part2", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    sample_answer = Answers.SAMPLE_PART1 if args.part2 else Answers.SAMPLE_PART2
    known_answer = Answers.SOLVED_PART2 if args.part2 else Answers.SOLVED_PART2

    input_file, expected_answer = ("sample.txt", sample_answer.value) if args.sample else ("input.txt", known_answer.value)
    print(f"Running configuration '{input_file}' expecting answer '{expected_answer}'")

    with open(f"./{input_file}", 'r') as fio:
        data = fio.read()

    answer = solve_puzzle(data, args.part2)

    if expected_answer and answer != expected_answer:
        raise AssertionError(f"{answer} is not equal to {expected_answer}")
    print(f"Answer is: {answer}")

if __name__ == "__main__":
    BOILERPLATE()
