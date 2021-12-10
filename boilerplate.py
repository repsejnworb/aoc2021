import unittest


def solve_puzzle(input: str):
    return "SAMPLE_ANSWER"


def main():
    with open('./input.txt') as fio:
        print(f"Answer is: {solve_puzzle(fio.read())}")


class TestSolution(unittest.TestCase):
    SAMPLE = "SAMPLEDATA\n"
    def test_part1(self):
        self.assertEqual(solve_puzzle(self.SAMPLE), 'SAMPLE_ANSWER')
    def test_part2(self):
        self.assertEqual(solve_puzzle(self.SAMPLE), 'SAMPLE_ANSWER')


if __name__ == '__main__':
    main()
