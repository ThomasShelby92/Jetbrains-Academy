s = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
player = "X"


def printer():
    print("---------")
    print(f"| {s[0][0]} {s[0][1]} {s[0][2]} |")
    print(f"| {s[1][0]} {s[1][1]} {s[1][2]} |")
    print(f"| {s[2][0]} {s[2][1]} {s[2][2]} |")
    print("---------")


def move(a):
    global player
    while True:
        x, y = input().split()
        try:
            x = int(x)
            y = int(y)
            if x > 3 or x < 1 or y > 3 or y < 1:
                print("Coordinates should be from 1 to 3!")
                continue
            if s[x - 1][y - 1] != " ":
                print("This cell is occupied! Choose another one!")
                continue
        except ValueError:
            print("You should enter numbers!")
            continue
        s[x - 1][y - 1] = a
        printer()
        if a == "X":
            player = "O"
        elif a == "O":
            player = "X"
        break


def check():

    x_win = 0
    o_win = 0
    x_c = 0
    o_c = 0

    while True:
        # check row
        for i in range(0, len(s)):
            if s[i][0] == "X" and s[i][1] == "X" and s[i][2] == "X":
                x_win = 1
            elif s[i][0] == "O" and s[i][1] == "O" and s[i][2] == "O":
                o_win = 1
        # check columns
        for i in range(0, len(s)):
            if s[0][i] == "X" and s[1][i] == "X" and s[2][i] == "X":
                x_win = 1
            elif s[0][i] == "O" and s[1][i] == "O" and s[2][i] == "O":
                o_win = 1

        # check diagonals
        if s[0][0] == "X" and s[1][1] == "X" and s[2][2] == "X":
            x_win = 1
        elif s[0][2] == "X" and s[1][1] == "X" and s[2][0] == "X":
            x_win = 1
        if s[0][0] == "O" and s[1][1] == "O" and s[2][2] == "O":
            o_win = 1
        elif s[0][2] == "O" and s[1][1] == "O" and s[2][0] == "O":
            o_win = 1

        if o_win == x_win == 1:
            return "Impossible"

        empty = 0
        for i in (range(0, len(s))):
            for j in range(0, len(s[i])):
                if s[i][j] == " ":
                    empty = 1
                if s[i][j] == "X":
                    x_c += 1
                if s[i][j] == 'O':
                    o_c += 1
        if abs(x_c - o_c) > 1:
            return "Impossible"
        if x_win == 1:
            return "X wins"
        elif o_win == 1:
            return "O wins"
        if empty == 1:

            return "Game not finished"
        else:
            return "Draw"


printer()
while True:
    move(player)
    if check() == "X wins" or check() == "O wins" or check() == "Draw":
        print(check())
        break
