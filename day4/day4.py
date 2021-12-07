import argparse
from itertools import chain

def sum_unmarked_on_board(board):
    return sum([sum(filter(None, row)) for row in filter(None, board)])

def mark(boards, number):
    for board in boards:
        for row in board:
            for index, value in enumerate(row):
                if value == number:
                    row[index] = None

def is_bingo_sequence(sequence):
    return all(x is None for x in sequence)

def board_has_bingo(board):
    offset = 5
    for i in range(5):
        step = i * offset
        if is_bingo_sequence(board[step:step+offset]):
            return True
        if is_bingo_sequence(board[i::offset]):
            return True
    return False

def display(boards):
    for board in boards:
        print("--------------------")
        for row in board:
            print(' '.join(map(str, row)))

ANSWER = None

parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
parser.add_argument("--part2", action="store_true")
args = parser.parse_args()

with open(f"./{args.inputfile}", 'r') as fio:
    _input = list(filter(None, fio.read().splitlines()))


draw_sequence = [int(v) for v in _input.pop(0).split(',')]
boards = []
finished_boards = []
chunk_size = 5
for i in range(0, len(_input), chunk_size):
    chunk = [list(map(int, row.split())) for row in _input[i:i+chunk_size]]
    boards.append(chunk)

display(boards)

for index, number in enumerate(draw_sequence):
    print(f"Status ({number}): boards({len(boards)}) finished({len(finished_boards)})")
    mark(boards, number)
    for board in boards:
        flat_board = list(chain.from_iterable(board))
        if board_has_bingo(flat_board):
            print(f"Winner {sum_unmarked_on_board(board)} on number {number}")
            finished_boards.append({"number":number, "board": board})
            boards.remove(board)

number, board = finished_boards[0].values()
if args.part2:
    number, board = finished_boards[-1].values()
ANSWER = sum_unmarked_on_board(board) * number
print(ANSWER)

