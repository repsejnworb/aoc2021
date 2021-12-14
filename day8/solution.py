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

############## PART1 FUNCTIONS

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



######### PART2 FUNCTIONS

def new_seven_segment_display():
    return {
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
}

def pattern_to_digit(pattern, configuration):
    ssd = new_seven_segment_display()
    for letter in pattern:
        segment = list(configuration.keys())[list(configuration.values()).index(letter)]
        ssd[segment] = letter
    return seven_segment_display_to_digit(ssd)


def letters(sevent_segment_display_dict):
    """ Returns the current letters of a seven segment display configuration """
    return "".join([v for v in sevent_segment_display_dict.values() if v])


def strip(string, characters):
    """ Returns string, stripped of any occurance of chars in characters """
    for character in characters:
        string = string.replace(character, "")
    return string


def seven_segment_display_to_digit(seven_segment_display):
    match list(seven_segment_display.values()):
        case [str(), str(), str(), None, str(), str(), str()]:
            return 0
        case [None, None, str(), None, None, str(), None]:
            return 1
        case [str(), None, str(), str(), str(), None, str()]:
            return 2
        case [str(), None, str(), str(), None, str(), str()]:
            return 3
        case [None, str(), str(), str(), None, str(), None]:
            return 4
        case [str(), str(), None, str(), None, str(), str()]:
            return 5
        case [str(), str(), None, str(), str(), str(), str()]:
            return 6
        case [str(), None, str(), None, None, str(), None]:
            return 7
        case [str(), str(), str(), str(), str(), str(), str()]:
            return 8
        case [str(), str(), str(), str(), None, str(), str()]:
            return 9
    raise AssertionError(f"Unmatchable: {seven_segment_display}")


def part2(input: str):
    lines = input.splitlines()
    sum = 0
    for line in lines:
        signal_patterns, digit_output = [v.split() for v in line.split('|')]
        configuration = new_seven_segment_display()

        signal_patterns = sorted(signal_patterns, key=len)
        pattern_groups = [list(g) for k, g in itertools.groupby(signal_patterns, key=len)]

        # 1 is free in the first group.
        digit_1_pattern = pattern_groups[0][0]
        configuration["BASE"] = digit_1_pattern
        
        # 7 is also nearly free in second group, minus digit_1_pattern
        # or rather, what is already stored in our configuration.
        digit_7_pattern = pattern_groups[1][0]
        configuration[1] = strip(digit_7_pattern, letters(configuration))

        # 4 is also a freebie. Once stripped it yields to letters that
        # plug into segment 2 and 4. We do not know the order yet so
        # we will store them in an extra key for stripping.
        pattern = pattern_groups[2][0]
        stripped = strip(pattern, letters(configuration))
        configuration["REMOVEME"] = stripped

        # The next group of len(5) can yield digits 5, 2 or 3. But we
        # care about it giving us the segments 5 and 7 in our configuration.
        # All three will, when stripped, yield one common letter that is
        # what goes into segment 7. 
        # One of them will, when stripped, yield another letter which goes
        # into segment 5.
        while configuration[5] is None:
            for pattern in pattern_groups[3]:
                stripped = strip(pattern, letters(configuration))
                if configuration[7] is None:
                    if len(stripped) == 1:
                        configuration[7] = stripped
                else:
                    if len(stripped) == 1:
                        configuration[5] = strip(stripped, letters(configuration))


        # Last step! The group of len(6) holds the key to finding out what letters
        # really go into segment 2 and 4. The magic happens when we encounter
        # the pattern for digit 0. This will be the one, when stripped, yields
        # only one letter. That letter will tell us what segment 2 really is
        # and allow us to know what segment 4 really is.
        # Let the battle for segment 2 begin!
        contestants = configuration["REMOVEME"]
        del configuration["REMOVEME"]
        for pattern in pattern_groups[4]:
            stripped = strip(pattern, letters(configuration))
            if len(stripped) == 1:
                # WINNER!
                configuration[2] = stripped
                configuration[4] = strip(contestants, stripped)

        # I lied above.. The group of len(6) is also the group where we can figure out the 
        # true order of the first pattern, segment 3 and 6.
        # The pattern that contains only one of them is the pattern for digit 6, which will
        # help us pinpoint segment 6. How romantic!
        # fml this code.. xD
        contestants = configuration["BASE"]
        del configuration["BASE"]
        for pattern in pattern_groups[4]:
            stripped = strip(pattern, letters(configuration))
            if len(stripped) == 1:
                # WINNER!
                configuration[6] = stripped
                configuration[3] = strip(contestants, stripped)

        digits = []
        for digit in digit_output:
            digits.append(pattern_to_digit(digit, configuration))
        sum += int("".join(map(str, digits)))
    
    return sum


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

    def test_sample_part1(self):
        self.assertEqual(part1(self.SAMPLE), 26)

    def test_smallsample_part2_1(self):
        self.assertEqual(part2(self._SAMPLE), 5353)

    def test_sample_part2(self):
        self.assertEqual(part2(self.SAMPLE), 61229)

    def test_puzzle_input_part1(self):
        puzzle_input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
        with puzzle_input_path.open() as fio:
            self.assertEqual(part1(fio.read()), 318)

    def test_puzzle_input_part2(self):
        puzzle_input_path = pathlib.Path(__file__).parent.resolve() / "input.txt"
        with puzzle_input_path.open() as fio:
            self.assertEqual(part2(fio.read()), 996280)


if __name__ == '__main__':
    main()
