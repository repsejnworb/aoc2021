import operator
from dataclasses import dataclass, field, InitVar, astuple

class _Vector2(type):
    @property
    def zero(cls):
        return cls(0, 1)
    @property
    def forward(cls):
        return cls(1, 0)
    @property
    def down(cls):
        return cls(0, 1)

@dataclass(order=True)
class Vector2(metaclass=_Vector2):
    x: int = 0
    y: int= 0
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
class Node:
    position: Vector2
    data: int = field(init=False, default=None)
    forward: int = field(init=False, default=None)
    down: int = field(init=False, default=None)
    marked: bool = field(init=False, default=None)
    matrix: InitVar[list[list]]
    debuglist: InitVar[list]
    def __post_init__(self, matrix, debuglist):
        print(self.position)
        try:
            self.data = matrix[self.position.y][self.position.x]
        except IndexError:
            try:
                self.position = Vector2.zero + Vector2.down
                self.data = matrix[self.position.y][self.position.x]
            except IndexError:
                return None
        debuglist.append(self)
        self.forward = Node(self.position + Vector2.forward, matrix, debuglist)
        #self.down = Node(self.position + Vector2.down, matrix, debuglist)


@dataclass
class Board:
    nodes: list[Node]


def parse_input(file: str, board_size: int): 
    draw_numbers = None
    boards = None

    with open(file, 'r') as fio:
        for line in fio:
            print(repr(line.split()))
            match len(line.split()):
                case 0:
                    print(0)

    return draw_numbers, boards

if __name__=='__main__':
    parse_input('./input.txt', 5)


def mtest(sequence):
    match len(sequence):
        case 0:
            print(f"0! {sequence}")
        case 4:
            print(f"4! {sequence}")
        case [*v]:
            print(f"X! {sequence}")

