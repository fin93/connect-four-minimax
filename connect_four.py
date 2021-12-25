import random
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


def is_full(boar, col):
    oke = False
    for i in range(board_rows):
        if boar[i][col] == "-":
            oke = True
    if oke:
        return False
    else:
        return True


def completely_full(boar):
    um = True
    for i in range(board_rows):
        for j in range(board_cols):
            if boar[i][j] == "-":
                um = False
    if not um:
        return False
    else:
        return True


def mark(boar, col, active_player):
    for i in range(board_rows):
        if boar[5][col] == "-":
            boar[5][col] = active_player
            break

        elif boar[i][col] != "-" and not is_full(boar, col):
            boar[i - 1][col] = active_player
            break


def check_if_won(boar, active):
    y_n = False
    for i in range(board_rows):
        for j in range(board_cols - 3):
            if boar[i][j] == boar[i][j + 1] and boar[i][j] == active:
                if boar[i][j] == boar[i][j + 2] and boar[i][j] == boar[i][j + 3]:
                    y_n = True
    for z in range(board_rows - 3):
        for y in range(board_cols):
            if boar[z][y] == boar[z + 1][y] and boar[z][y] == active:
                if boar[z][y] == boar[z + 2][y] and boar[z][y] == boar[z + 3][y]:
                    y_n = True
    for k in range(board_rows - 3):
        for u in range(board_cols - 3):
            if boar[k][u] == boar[k + 1][u + 1] and boar[k][u] == active:
                if board[k][u] == boar[k + 2][u + 2] and boar[k][u] == boar[k + 3][u + 3]:
                    y_n = True
    for d in range(3, board_rows):
        for lo in range(board_cols - 3):
            if boar[d][lo] == boar[d - 1][lo + 1] and boar[d][lo] == active:
                if boar[d][lo] == boar[d - 2][lo + 2] and boar[d][lo] == boar[d - 3][lo + 3]:
                    y_n = True
    if y_n:
        return True
    else:
        return False


def comp_move(boar, player):
    best_score = -1000
    best_move = 0
    for i in range(board_cols):
        for j in range(board_rows):
            if boar[5][i] == "-":
                boar[5][i] = player
                score = minimax(boar, False, 1)
                boar[5][i] = "-"
                if score > best_score:
                    best_score = score
                    best_move = i

            elif boar[j][i] != "-" and not is_full(boar, i):
                boar[j - 1][i] = player
                score = minimax(boar, False, 1)
                boar[j - 1][i] = "-"
                if score > best_score:
                    best_score = score
                    best_move = i

    mark(boar, best_move, player_o)


def minimax(boar, is_max, depth):

    if check_if_won(boar, player_o):
        return 100
    elif check_if_won(boar, player_x):
        return -100
    elif completely_full(boar):
        return 0

    if is_max:
        best_score = -1000
        for i in range(board_cols):
            for j in range(board_rows):
                if boar[5][i] == "-":
                    boar[5][i] = player_o
                    score = minimax(boar, False, depth + 1)
                    boar[5][i] = "-"
                    if score > best_score:
                        best_score = score
                elif boar[j][i] != "-" and not is_full(boar, i):
                    boar[j - 1][i] = player_o
                    score = minimax(boar, False, depth + 1)
                    boar[j - 1][i] = "-"
                    if score > best_score:
                        best_score = score
        return best_score

    else:
        best_score = 1000
        for i in range(board_cols):
            for j in range(board_rows):
                if boar[5][i] == "-":
                    boar[5][i] = player_x
                    score = minimax(boar, True, depth + 1)
                    boar[5][i] = "-"
                    if score < best_score:
                        best_score = score
                elif boar[j][i] != "-" and not is_full(boar, i):
                    boar[j - 1][i] = player_x
                    score = minimax(boar, True, depth + 1)
                    boar[j - 1][i] = "-"
                    if score < best_score:
                        best_score = score
        return best_score


def main():
    active = player_x
    while True:
        if active == player_x:
            mark(board, int(input("Enter a column [1-7]: ")) - 1, player_x)
            print_board(board)
            active = player_o
        elif active == player_o:
            comp_move(board, player_o)
            print_board(board)
            active = player_x


if __name__ == '__main__':
    main()
