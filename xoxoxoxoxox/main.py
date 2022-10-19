# Functions


def print_grid():
    for i in range(3):
        for j in range(3):
            print(
                "|" + ("X" if grid[i][j] == 1 else "O" if grid[i][j] == -1 else "-"), end="")
        print("|")


def get_input():
    player = input("Enter action: ")
    if player.isnumeric():
        return int(player) - 1
    else:
        return -1


def update():
    while True:
        action = get_input()
        if action >= 0 and action <= 8:
            if grid[action//3][action % 3] == 0:
                grid[action//3][action % 3] = turn
                return turn * -1
            else:
                print("Invalid action")
        else:
            print("Invalid action")


def check_win():
    draw = True
    for i in range(3):
        if grid[i][0] == grid[i][1] == grid[i][2] != 0:
            return grid[i][0]
        if grid[0][i] == grid[1][i] == grid[2][i] != 0:
            return grid[0][i]
        for j in range(3):
            if grid[i][j] == 0:
                draw = False
    if grid[0][0] == grid[1][1] == grid[2][2] != 0:
        return grid[0][0]
    if grid[0][2] == grid[1][1] == grid[2][0] != 0:
        return grid[0][2]
    if draw:
        return 2
    return 0


# Init
grid = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
turn = 1

# Main loop
while True:
    print_grid()
    turn = update()
    win = check_win()
    if win != 0: # 0 = no win, 1 = X win, -1 = O win, 2 = tie
        print_grid()
        if win == 2:
            print("TIE")
        else:
            if win == 1:
                print("Player X wins!")
            else:
                print("Player O wins!")
        break
