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

def get_bingo_board(boards):
    for board in boards:
        flat_board = list(chain.from_iterable(board))
        if board_has_bingo(flat_board):
            return board

ANSWER = None

parser = argparse.ArgumentParser()
parser.add_argument("inputfile")
args = parser.parse_args()

with open(f"./{args.inputfile}", 'r') as fio:
    _input = list(filter(None, fio.read().splitlines()))


draw_sequence = [int(v) for v in _input.pop(0).split(',')]
boards = []
chunk_size = 5
for i in range(0, len(_input), chunk_size):
    chunk = [list(map(int, row.split())) for row in _input[i:i+chunk_size]]
    boards.append(chunk)

for number in draw_sequence:
    mark(boards, number)
    winner_board = get_bingo_board(boards)
    if winner_board:
        ANSWER = sum_unmarked_on_board(winner_board) * number
        break

print(ANSWER)

