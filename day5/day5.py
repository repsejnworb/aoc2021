import argparse
from dataclasses import dataclass, field, fields, astuple
from itertools import filterfalse

@dataclass(order=True, frozen=True)
class Vector2():
    x: int = 0
    y: int = 0

    def __add__(self, other):
        return Vector2(*(getattr(self, dim.name)+getattr(other, dim.name) for dim in fields(self)))

    def __sub__(self, other):
        return Vector2(*(getattr(self, dim.name)-getattr(other, dim.name) for dim in fields(self)))

    def __mul__(self, other):
        return Vector2(*(getattr(self, dim.name)*other for dim in fields(self)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __iter__(self):
        return iter(astuple(self))


@dataclass
class Line():
    start: Vector2
    end: Vector2
    points: list[Vector2] = field(init=False, default_factory=list)

    def __post_init__(self):
        diff = self.end - self.start
        print(f"{self.start} -> {self.end} ({diff})")


def parse_data(data):
    lines = []
    for row in data.splitlines():
        line = [list(map(int, point.split(','))) for point in row.split(' -> ')]
        line = Line(*[Vector2(*point) for point in line])
        lines.append(line)
    return lines


def is_diagonal(line):
    if line.start.x == line.end.x or line.start.y == line.end.y:
        return False
    return True


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputfile")
    parser.add_argument("--part2", action="store_true")
    args = parser.parse_args()

    with open(f"./{args.inputfile}", 'r') as fio:
        lines = parse_data(fio.read())
    
    filtered_lines = list(filterfalse(is_diagonal, lines))
    import code
    code.interact(local=locals())
    #covered_points = 


if __name__ == "__main__":
    main()
