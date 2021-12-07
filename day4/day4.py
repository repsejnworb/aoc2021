from __future__ import annotations
import operator
from dataclasses import dataclass, field, InitVar, astuple, fields

class _Vector2(type):

    @property
    def zero(cls):
        return cls(0, 0)

    @property
    def forward(cls):
        return cls(1, 0)

    @property
    def down(cls):
        return cls(0, 1)

@dataclass(order=True, frozen=True)
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
    data: int
    left: Node = field(init=False, default=None)
    right: Node = field(init=False, default=None)
    up: Node = field(init=False, default=None)
    down: Node = field(init=False, default=None)
    marked: bool = field(init=False, default=False)

    def create_links(self, nodes: dict[Node]):
        self.left = nodes.get(self.position - Vector2.forward)
        self.right = nodes.get(self.position + Vector2.forward)
        self.down = nodes.get(self.position + Vector2.down)
        self.up = nodes.get(self.position - Vector2.down)

    def is_bingo(self, direction):
        yield self.marked
        _next = getattr(self, direction)
        if _next:
            yield from getattr(self, direction).is_bingo(direction)

@dataclass
class Edge(Node):
    position: Vector2 = Vector2(-1, -1)
    data: int = -1

    def __repr__(self):
        return self.__class__.__qualname__



@dataclass
class Board:
    head: Node = field(init=False, default=None)
    nodes: dict[Node] = field(init=False, default_factory=dict)
    size: Vector2 = field(init=False, default=Vector2.zero)
    matrix: InitVar[list[list]]

    # jank :<
    def __post_init__(self, matrix):
        self.size = Vector2(len(matrix[0]), len(matrix))
        for y, row in enumerate(matrix):
            for x, column in enumerate(row): 
                node = Node(Vector2(x,y), column)
                if self.head is None:
                    self.head = node
                self.nodes[node.position] = node
        for node in self.nodes.values():
            node.create_links(self.nodes)

    # jaaaaaaaaaaaaank :< sunk cost fallacy, just wanna finish now with this
    # stupidly convuluted solution
    def has_bingo(self):
        for pos, node in self.nodes.items():

            # vertical check for each node in first row
            if pos.y == 0:
                result = all(node.is_bingo("down"))
                if result:
                    return result

            # horizontal check for each node in first column
            if pos.x == 0:
                result = all(node.is_bingo("right"))
                if result:
                    return result

        return False

    def mark_node(self, number):
        for node in self.nodes.values():
            if node.data == number:
                node.marked = True

    def sum_unmarked(self):
        return sum([node.data for node in self.nodes.values() if node.marked])

    def run(self, number):
        self.mark_node(number)
        if self.has_bingo():
            return number * self.sum_unmarked()



def parse_input(file: str, board_size: int): 
    draw_sequence = []
    boards = []

    with open(file, 'r') as fio:
        tmp_matrix = []
        for line in fio:
            print(repr(line.split()))
            match len(line.split()):
                case 0:
                    pass
                case 5:
                    if len(tmp_matrix) == 5:
                        boards.append(Board(tmp_matrix))
                        tmp_matrix = []
                    tmp_matrix.append([int(v) for v in line.split()])
                case _:
                    draw_sequence += [int(v) for v in line.split(',')]

    print(f"returning {len(draw_sequence)} sequence")
    print(f"returning {len(boards)} num boards")

    return draw_sequence, boards

if __name__=='__main__':
    draw_sequence, boards = parse_input('./input.txt', 5)
    # draw_sequence = [1,2,3,4,5,6]
    # boards = []
    # boards.append(Board([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    # boards.append(Board([[1,2], [3,4]]))
    result = None
    for number in draw_sequence:
        for board in boards:
            result = board.run(number)
            if result:
                break
        if result:
            break
    print(result)
    import code
    code.interact(local=locals())


    



def mtest(sequence):
    match len(sequence):
        case 0:
            print(f"0! {sequence}")
        case 4:
            print(f"4! {sequence}")
        case [*v]:
            print(f"X! {sequence}")

