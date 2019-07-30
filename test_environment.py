import itertools
from numpy import sum

"""
Riddle:
Consider a 5x5 chess board. Is it possible to place five queens
on the board such that three pawns can safely be placed on the
board? In other words, by carefully choosing where to place the
five queens, can you arrange it so that there are three squares
on the board that non eof the queens can attack?
"""


def diagonal_check(queen_position, test_position):
    if queen_position[0] + queen_position[1] == test_position[0] + test_position[1]:
        return True
    elif queen_position[0] - queen_position[1] == test_position[0] - test_position[1]:
        return True
    else:
        return False


def horizontal_check(queen_position, test_position):
    if queen_position[0] == test_position[0]:
        return True
    elif queen_position[1] == test_position[1]:
        return True
    else:
        return False


def chess_quest(board_size, queens, pawns):

    solution_count = 0
    board_positions = []

    for each in range(board_size):
        for column in range(board_size):
            board_positions.append((each, column))

    for positions in itertools.combinations(board_positions, queens):

        test_board = []
        for each in range(board_size):
            test_board.append([1] * board_size)

        for row in range(board_size):
            for column in range(board_size):
                for position in positions:

                    if diagonal_check(position, (row, column)):
                        test_board[row][column] = 0
                    if horizontal_check(position, (row, column)):
                        test_board[row][column] = 0

        if sum(sum(test_board, 0), 0) >= pawns:
            solution_count += 1
            for row in range(board_size):
                for column in range(board_size):

                    if test_board[row][column] == 1:
                        test_board[row][column] = 'P'
                    if (row, column) in positions:
                        test_board[row][column] = 'Q'
                    elif test_board[row][column] == 0:
                        test_board[row][column] = ' '

            print('Solution ' + str(solution_count))
            for row in test_board:
                print(*row, sep='|')
            print()


chess_quest(5, 5, 3)
