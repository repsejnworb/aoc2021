import argparse
from dataclasses import dataclass, field, fields, astuple
from itertools import filterfalse
import math

@dataclass(order=True, frozen=True)
class Vector2():
    x: int = 0
    y: int = 0

    def __add__(self, other):
        return Vector2(*(getattr(self, dim.name)+getattr(other, dim.name) for dim in fields(self)))

    def __sub__(self, other):
        return Vector2(*(getattr(self, dim.name)-getattr(other, dim.name) for dim in fields(self)))

    def __mul__(self, other):
        if isinstance(other, Vector2):
            return Vector2(*(getattr(self, dim.name)*getattr(other, dim.name) for dim in fields(self)))
        else:
            return Vector2(*(getattr(self, dim.name)*other for dim in fields(self)))

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(*(getattr(self, dim.name)/getattr(other, dim.name) for dim in fields(self)))
        else:
            return Vector2(*(getattr(self, dim.name)/other for dim in fields(self)))

    def __floordiv__(self, other):
        if isinstance(other, Vector2):
            return Vector2(*(getattr(self, dim.name)//getattr(other, dim.name) for dim in fields(self)))
        else:
            return Vector2(*(getattr(self, dim.name)//other for dim in fields(self)))

    def __iter__(self):
        return iter(astuple(self))

    def magnitude(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def round(self):
        return Vector2(round(self.x), round(self.y))



@dataclass
class Line():
    start: Vector2
    end: Vector2
    points_between: list[Vector2] = field(init=False, default_factory=list)

    def __post_init__(self):
        points = []
        diff = self.end - self.start
        step = diff / diff.magnitude()
        # as we only want to work with whole numbers
        step = step.round()

        point = self.start + step
        while point != self.end:
            self.points_between.append(point)
            point += step

    def points(self):
        return [self.start] + self.points_between + [self.end]



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

    ### DEBUG STUFF
    kiss = lines[-1]
    s = kiss.start
    e = kiss.end
    import code
    code.interact(local=dict(globals(), **locals()))
    ### DEBUG STUFF


if __name__ == "__main__":
    main()
