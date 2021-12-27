import copy
import os

board_cols = 7
board_rows = 6
player_o = "o"
player_x = "x"
board = [
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"],
    ["-", "-", "-", "-", "-", "-", "-"]
]


def print_board(boar):
    for i in range(board_rows):
        for j in range(board_cols):
            print(boar[i][j], end=" ")
        print()


def is_col_full(boar, col):
    for i in range(board_rows):
        if boar[i][col] == "-":
            return False
    return True


def is_whole_full(boar):
    for i in range(board_rows):
        for j in range(board_cols):
            if boar[i][j] == "-":
                return False
    return True


def mark(boar, col, active_player):
    for i in range(board_rows):
        if boar[5][col] == "-":
            boar[5][col] = active_player
            break
        elif boar[i][col] != "-" and not is_col_full(boar, col):
            boar[i - 1][col] = active_player
            break


def has_won(boar, active):
    for i in range(board_rows):
        for j in range(board_cols):
            if boar[i][j - 3] == boar[i][j - 2] and boar[i][j - 3] == boar[i][j - 1]:
                if boar[i][j - 3] == boar[i][j] and boar[i][j - 3] == active:
                    return True
            if boar[i - 3][j] == boar[i - 2][j] and boar[i - 3][j] == boar[i - 1][j]:
                if boar[i - 3][j] == boar[i][j] and boar[i - 3][j] == active:
                    return True
            if boar[i - 3][j - 3] == boar[i - 2][j - 2] and boar[i - 3][j - 3] == boar[i - 1][j - 1]:
                if boar[i - 3][j - 3] == boar[i][j] and boar[i - 3][j - 3] == active:
                    return True
            if boar[5 - i][j - 3] == boar[4 - i][j - 2] and boar[5 - i][j - 3] == boar[3 - i][j - 1]:
                if boar[5 - i][j - 3] == boar[2 - i][j] and boar[5 - i][j - 3] == active:
                    return True
    return False


def has_three(boar, active):
    for i in range(board_rows):
        for j in range(board_cols):
            if boar[i][j - 3] == boar[i][j - 2] and boar[i][j - 3] == boar[i][j - 1]:
                if boar[i][j - 3] == active:
                    return True
            if boar[i - 3][j] == boar[i - 2][j] and boar[i - 3][j] == boar[i - 1][j]:
                if boar[i - 3][j] == active:
                    return True
            if boar[i - 3][j - 3] == boar[i - 2][j - 2] and boar[i - 3][j - 3] == boar[i - 1][j - 1]:
                if boar[i - 3][j - 3] == active:
                    return True
            if boar[5 - i][j - 3] == boar[4 - i][j - 2] and boar[5 - i][j - 3] == boar[3 - i][j - 1]:
                if boar[5 - i][j - 3] == active:
                    return True
    return False


def has_two(boar, active):
    for i in range(board_rows):
        for j in range(board_cols):
            if boar[i][j - 3] == boar[i][j - 2] and boar[i][j - 3] == active:
                return True
            if boar[i - 3][j] == boar[i - 2][j] and boar[i - 3][j] == active:
                return True
            if boar[i - 3][j - 3] == boar[i - 2][j - 2] and boar[i - 3][j - 3] == active:
                return True
            if boar[5 - i][j - 3] == boar[4 - i][j - 2] and boar[5 - i][j - 3] == active:
                return True
    return False


def comp_move(boar, player):
    best_score = -10000
    worst_score = 10000
    best_move = 0
    for i in range(board_cols):
        copy_boar = copy.deepcopy(boar)
        mark(copy_boar, i, player)
        score = minimax(copy_boar, False, 0)
        if score > best_score:
            best_score = score
            best_move = i

    mark(board, best_move, player_o)


def minimax(boar, is_max, depth):
    if depth < 4:
        if has_won(boar, player_o):
            return 1000
        elif has_won(boar, player_x):
            return -1000
        if has_three(boar, player_o):
            return 100
        elif has_three(boar, player_x):
            return -100

        if is_whole_full(boar):
            return 0

        if is_max:
            best_score = -10000
            for i in range(board_cols):
                copy_boar = copy.deepcopy(boar)
                mark(copy_boar, i, player_o)
                score = minimax(copy_boar, False, depth + 1)
                if score > best_score:
                    best_score = score
            return best_score

        else:
            best_score = 10000
            for i in range(board_cols):
                copy_boar = copy.deepcopy(boar)
                mark(copy_boar, i, player_x)
                score = minimax(boar, True, depth + 1)
                if score < best_score:
                    best_score = score
            return best_score
    x = 0
    if has_won(boar, player_o):
        x += 1000
    elif has_won(boar, player_x):
        x -= 1000
    if has_three(boar, player_o):
        x += 100
    elif has_three(boar, player_x):
        x -= 100
    if has_two(boar, player_o):
        x += 10
    if has_two(boar, player_x):
        x -= 10
    elif is_whole_full(boar):
        x = 0
    return x


def main():
    active = player_x
    for i in range(board_rows):
        for j in range(board_cols):
            board[i][j] = "-"

    while True:
        if active == player_x:
            mark(board, int(input("Enter a column[1-7]: ")) - 1, player_x)
            os.system("cls")
            print_board(board)
            if has_won(board, active):
                break
            active = player_o
        elif active == player_o:
            comp_move(board, player_o)
            os.system("cls")
            print_board(board)
            if has_won(board, active):
                break
            active = player_x
    print(f"{active} has won!")
    if input("Do you want to play again [y/n]: ").lower() == "y":
        main()


if __name__ == '__main__':
    main()
