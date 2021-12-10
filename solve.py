import argparse
from importlib.machinery import SourceFileLoader
import inspect
from itertools import filterfalse
import sys
from pathlib import Path

SOLUTION_INTERFACE = {
    "variables": [
        "SAMPLE_PART1",
        "SAMPLE_PART2",
        "SOLVED_PART1",
        "SOLVED_PART2",
    ],
    "functions": [
        {
            "name": "solve_puzzle",
            "args": ["data", "part2"]
        }
    ]
}

def verify_implemented(solution):
    """ Verifies that a solution file implements expected variables
    and functions. """
    result = {}
    for variable in SOLUTION_INTERFACE["variables"]:
        result[variable] = hasattr(solution, variable)

    for function in SOLUTION_INTERFACE["functions"]:
        result[function["name"]] = hasattr(solution, function["name"])
        if result[function["name"]]:
            parameters = inspect.signature(getattr(solution, function["name"])).parameters
            for arg in function["args"]:
                result[f'{function["name"]}.{arg}'] = arg in parameters.keys()

    implemented = any(result.values())
    return implemented, result


    #signature = inspect.signature()


def get_file_paths(input_location):
    paths = {
        "directory": Path(input_location),
        "solution": Path(input_location) / "solution.py",
        "puzzle_input": Path(input_location) / "puzzle_input.txt",
        "sample_input": Path(input_location) / "sample_input.txt",
    }
    return paths


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("solution_location")
    parser.add_argument("--sample", action="store_true")
    parser.add_argument("--part2", action="store_true")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    paths = get_file_paths(args.solution_location)
    if missing_files := list(filterfalse(lambda p: p.exists(), paths.values())):
        for missing in missing_files:
            print(f"Couldn't find required file: {missing}")
        sys.exit(1)

    solution_folder = Path(args.solution_location)
    puzzle_input_path = solution_folder / "input.txt"
    sample_input_path = solution_folder / "sample.txt"

    try:
        #solution = importlib.import_module(args.day)
        solution = SourceFileLoader("kiss", str(solution_location))
        print(solution.is_package("kiss"))
    except ModuleNotFoundError as e:
        print(f"Couldn't find a solution named '{args.day}''")
        sys.exit(1)

    breakpoint()

    implemented, result = verify_implemented(solution)
    breakpoint()
    if not implemented:
        print(f"Solution '{solution}' has not implemented:")
        for expected_attr, _ in filterfalse(lambda r: r[1], result.items()):
            print(end=" * ")
            print(f"'{expected_attr}' not implemented.")
        sys.exit(1)


    #solution_directory = Path(solution.__file__).parent
    #puzzle_input_path = solution_directory / "input.txt"
    #sample_input_path = solution_directory / "sample.txt"


    sample_answer = solution.SAMPLE_PART1 if args.part2 else solution.SAMPLE_PART2
    known_answer = solution.SOLVED_PART2 if args.part2 else solution.SOLVED_PART2

    input_path, expected_answer = (sample_input_path, sample_answer) if args.sample else (puzzle_input_path, known_answer)
    print(f"Running configuration '{input_file}' expecting answer '{expected_answer}'")

    with input_path.open() as fio:
        data = fio.read()

    answer = solution.solve_puzzle(data, args.part2)

    if expected_answer and answer != expected_answer:
        raise AssertionError(f"{answer} is not equal to {expected_answer}")
    print(f"Answer is: {answer}")

if __name__ == "__main__":
    main()
