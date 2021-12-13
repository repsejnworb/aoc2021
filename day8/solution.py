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

def new_digit_map():
    return {
    0: None,
    1: None,
    2: None,
    3: None,
    4: None,
    5: None,
    6: None,
    7: None,
    8: None,
    9: None,
}


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


def to_str_or_n(value):
    """ Returns str('n') if 'value' is None else str(value) """
    return '.' if value is None else str(value)


def print_seven_segment_display(sequence):
    s1, s2, s3, s4, s5, s6, s7 = map(to_str_or_n, sequence)
    empty = " "
    print(f" {s1 * 4} \n" \
            f"{s2}{empty * 4}{s3}\n" \
            f"{s2}{empty * 4}{s3}\n" \
            f" {s4 * 4} \n" \
            f"{s5}{empty * 4}{s6}\n" \
            f"{s5}{empty * 4}{s6}\n" \
            f" {s7 * 4} ")



def ____OLD__part2(input: str):
    lines = input.splitlines()
    digits = []
    for line in lines:
        signal_patterns, digit_output = [v.split() for v in line.split('|')]
        # find the code for '8'
        config_code = [code for code in itertools.chain(signal_patterns, digit_output) if len(code) == 8][0]
        print(config_code)
        break

    return "NotSolved"





def ______part2(input: str):
    lines = input.splitlines()
    digits = []
    for line in lines:
        print(line)
        signal_patterns, digit_output = [v.split() for v in line.split('|')]
        configuration = new_seven_segment_display()

        for code in signal_patterns:
            match len(code):
                case 2:
                    #### g=1, 3  f=2, 7
                    # matched a 1
                    configuration[3] = code[0]
                    configuration[6] = code[1]
                    print(configuration[3] + " " + configuration[6])
                case 3:
                    # matched a 7
                    configuration[1] = code[0]
                    configuration[3] = code[1]
                    configuration[6] = code[2]
                    print(configuration[1] + " " + configuration[3] + " " + configuration[6])
                case 4:
                    configuration[2] = code[0]
                    configuration[3] = code[1]
                    configuration[4] = code[2]
                    configuration[6] = code[3]
                    print(configuration[2] + " " + configuration[3] + " " + configuration[4] + " " + configuration[6])

        print(configuration)
        from collections import Counter
        c = Counter(configuration.values())
        print(f"Counter: {c}")
        break
    
    return "No solved"


korvdict = {

}

def part2(input: str):
    lines = input.splitlines()
    digits = []
    for line in lines:
        print(line)
        signal_patterns, digit_output = [v.split() for v in line.split('|')]
        configuration = new_seven_segment_display()
        digit_map = new_digit_map()

        signal_patterns = sorted(signal_patterns, key=len)
        pattern_groups = [list(g) for k, g in itertools.groupby(signal_patterns, key=len)]

        # 1 is free in the first group.
        digit_1_pattern = pattern_groups[0][0]
        configuration[3] = digit_1_pattern[0]
        configuration[6] = digit_1_pattern[1]
        
        # 7 is also nearly free in second group, minus digit_1_pattern
        # or rather, what is already stored in our configuration.
        digit_7_pattern = pattern_groups[1][0]
        print(f"CASE3 PATTERN: {digit_7_pattern} and stripping: {configuration}")
        configuration[1] = strip(digit_7_pattern, letters(configuration))

        # 4 is also a freebie. Once stripped it yields to letters that
        # plug into segment 2 and 4. We do not know the order yet so
        # we will store them in an extra key for stripping.
        pattern = pattern_groups[2][0]
        stripped = strip(pattern, letters(configuration))
        print(f"CASE4 PATTERN: {pattern} and stripping: {configuration} (and stripped: {stripped}")
        #configuration["REMOVEME"] = stripped
        configuration[2] = stripped[0]
        configuration[4] = stripped[1]

        # The next group of len(5) can yield digits 5, 2 or 3. But we
        # care about it giving us the segments 5 and 7 in our configuration.
        # All three will, when stripped, yield one common letter that is
        # what goes into segment 7. 
        # One of them will, when stripped, yield another letter which goes
        # into segment 5.
        while configuration[5] is None:
            for pattern in pattern_groups[3]:
                stripped = strip(pattern, letters(configuration))
                print(stripped)
                if configuration[7] is None:
                    if len(stripped) == 1:
                        configuration[7] = stripped
                    else:
                        print(f"LEN: {len(stripped)} and stripped: {stripped}")
                        print("####1111111############################################")
                        print("BAAAAAAAAAAAAAAAD TIMES MATE")
                else:
                    if len(stripped) == 1:
                        configuration[5] = strip(stripped, letters(configuration))
                    elif len(stripped) == 0:
                        # previous go around already sorted 5
                        pass
                    else:
                        print(f"LEN: {len(stripped)} and stripped: {stripped}")
                        print("######222222222222##########################################")
                        print("BAAAAAAAAAAAAAAAD TIMES MATE")

        # for pattern in signal_patterns:
        #     match len(pattern):
        #         case 2:
        #             configuration[3] = pattern[0]
        #             configuration[6] = pattern[1]
        #             digit_map[1] = pattern
        #         case 3:
        #             print(f"CASE3 PATTERN: {pattern} and stripping: {configuration}")
        #             configuration[1] = strip(pattern, letters(configuration))
        #             digit_map[7] = pattern
        #         case 4:
        #             # Can't know for sure where in the config this goes yet.
        #             # But storing it for reference for upcoming cases
        #             print(f"CASE4 PATTERN: {pattern} and stripping: {configuration}")
        #             stripped = strip(pattern, letters(configuration))
        #             korvdict["kroken"] = stripped
        #             configuration[2] = stripped[0]
        #             configuration[4] = stripped[1]
        #             print(korvdict["kroken"])
        #             digit_map[4] = pattern
        #         case 5:
        #             print(f"CASE5 PATTERN: {pattern} and stripping: {configuration}")
        #             stripped = strip(pattern, letters(configuration))
        #             print(stripped)
        #             if configuration[7] is None:
        #                 if len(stripped) == 1:
        #                     configuration[7] = stripped
        #                 else:
        #                     print(f"LEN: {len(stripped)} and stripped: {stripped}")
        #                     print("####1111111############################################")
        #                     print("BAAAAAAAAAAAAAAAD TIMES MATE")
        #             else:
        #                 if len(stripped) == 1:
        #                     configuration[5] = strip(stripped, letters(configuration))
        #                 elif len(stripped) == 0:
        #                     # previous go around already sorted 5
        #                     pass
        #                 else:
        #                     print(f"LEN: {len(stripped)} and stripped: {stripped}")
        #                     print("######222222222222##########################################")
        #                     print("BAAAAAAAAAAAAAAAD TIMES MATE")

        print(digit_map)
        print(configuration)
        print("&&&&&&&&&&&&&&&&&&&&&&")
        digits = []
        for digit in digit_output:
            digits.append(pattern_to_digit(digit, configuration))
        print("".join(map(str, digits)))
        print("€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€€")
        
    import code
    code.interact(local=locals())
    
    return "No solved"



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
    def Festtest_part2_1(self):
        self.assertEqual(part2(self._SAMPLE), 5353)

    def test_part2_2(self):
        self.assertEqual(part2(self.SAMPLE), 61229)


if __name__ == '__main__':
    main()
