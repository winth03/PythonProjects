class Model:
    def __init__(self):
        self.grid = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
        ]

class View:
    def __init__(self, model):
        self.grid = model.grid

    def print_grid(self):
        for i in range(3):
            for j in range(3):
                print("|" + ("X" if self.grid[i][j] == 1 else "O" if self.grid[i][j] == -1 else "-"), end="")
            print("|")

class Controller:
    def __init__(self, model):
        self.grid = model.grid
        self.turn = 1

    def get_input(self):
        return int(input("Enter action: ")) - 1

    def update(self):
        while True:
            action = self.get_input()
            if self.grid[action//3][action%3] == 0 and action >= 0 and action <= 8:
                self.grid[action//3][action%3] = self.turn
                self.turn *= -1
                break
            else:
                print("Invalid action")

    def check_win(self):
        draw = True
        for i in range(3):
            if self.grid[i][0] == self.grid[i][1] == self.grid[i][2] != 0:
                return self.grid[i][0]
            if self.grid[0][i] == self.grid[1][i] == self.grid[2][i] != 0:
                return self.grid[0][i]
            for j in range(3):
                if self.grid[i][j] == 0:
                    draw = False
        if self.grid[0][0] == self.grid[1][1] == self.grid[2][2] != 0:
            return self.grid[0][0]
        if self.grid[0][2] == self.grid[1][1] == self.grid[2][0] != 0:
            return self.grid[0][2]
        if draw:
            return 0

# Init
model = Model()
view = View(model)
controller = Controller(model)

# Main loop
while True:
    view.print_grid()
    controller.update()
    win = controller.check_win() # none, 1, -1, 0
    if win:
        view.print_grid()
        print("Player " + ("X" if win == 1 else "O") + " wins!")
        break
    elif win == 0:
        view.print_grid()
        print("Draw!")
        break
    