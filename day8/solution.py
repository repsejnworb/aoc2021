import itertools
import pathlib
import unittest

""" 
OG RENDERING:
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

"""

DIGIT_MAP = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


class SevenSegmentDisplay:
    def __init__(self):
        # q == None
        self.segment1 = "q"
        self.segment2 = "q"
        self.segment3 = "q"
        self.segment4 = "q"
        self.segment5 = "q"
        self.segment6 = "q"
        self.segment7 = "q"

    def is_complete(self):
        """ Returns True if all segments has been set, 
        which means they are no longer of value 'q' """
        return all([getattr(self, f"segment{i}") != 'q' for i in range(1, 8)])

    def __str__(self):
        empty = " "
        return f" {self.segment1 * 4} \n" \
                f"{self.segment2}{empty * 4}{self.segment3}\n" \
                f"{self.segment2}{empty * 4}{self.segment3}\n" \
                f" {self.segment4 * 4} \n" \
                f"{self.segment5}{empty * 4}{self.segment6}\n" \
                f"{self.segment5}{empty * 4}{self.segment6}\n" \
                f" {self.segment7 * 4} " \


def lookup_unique_digit(code: str):
    matches = [k for k,v in DIGIT_MAP.items() if len(v) == len(code)]
    if len(matches) > 1:
        return None
    else:
        return matches[0]


def part1(input: str):
    lines = input.splitlines()
    digits = []
    for line in lines:
        signal_patterns, digit_output = [v.split() for v in line.split('|')]
        for code in digit_output:
            digit = lookup_unique_digit(code)
            if digit is not None:
                digits.append(digit)
    return len(digits)


def part2(input: str):
    lines = input.splitlines()
    digits = []
    for line in lines:
        signal_patterns, digit_output = [v.split() for v in line.split('|')]
        # find the code for '8'
        config_code = [code for code in itertools.chain(signal_patterns, digit_output) if len(code) == 8][0]
        print(config_code)
        break

    return "NotSolved"


def main():
    puzzle_input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
    with puzzle_input_path.open() as fio:
        input = fio.read()
    print(f"Part1 answer is: {part1(input)}")
    print(f"Part2 answer is: {part2(input)}")


class TestSolution(unittest.TestCase):
    _SAMPLE = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf\n"
    SAMPLE = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

    def test_part1(self):
        self.assertEqual(part1(self.SAMPLE), 26)
    def test_part2(self):
        self.assertEqual(part2(self.SAMPLE), 5353)


if __name__ == '__main__':
    main()
