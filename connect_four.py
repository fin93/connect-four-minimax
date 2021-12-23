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


def main():
    active = player_x
    while True:
        if active == player_x:
            active = player_o
            pass
        elif active == player_o:
            active = player_x
            pass


if __name__ == '__main__':
    main()
