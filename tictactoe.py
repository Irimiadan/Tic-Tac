import os
class TicTacToe:

    def __init__(self):
        self.input = ""
        self.board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.test_board = []
        self.game_state = None
        self.player = "X"
        self.gamedone = None

    def print_header(self):
	    print("""
 _____  _  ____     _____  ____  ____     _____  ____  _____        1 3 | 2 3 | 3 3
/__ __\/ \/   _\   /__ __\/  _ \/   _\   /__ __\/  _ \/  __/            |     |
  / \  | ||  / _____ / \  | / \||  / _____ / \  | / \||  \          1 2 | 2 2 | 3 2
  | |  | ||  \_\____\| |  | |-|||  \_\____\| |  | \_/||  /_             |     |
  \_/  \_/\____/     \_/  \_/ \|\____/     \_/  \____/\____\        1 1 | 2 1 | 3 1

 To play Tic-Tac-Toe, you need to get three in a row...
 Your choices are defined through coordinates, they must be in x y form ... \n \n """)

    def next_turn(self):
        if self.player == "X":
            self.player = "O"
        elif self.player == "O":
            self.player = "X"


    def print_board(self):
        print("\n\t\t---------")
        for col in range(3):
            print("\t\t| ", end= "")
            for row in range(3):
                if row == 2:
                    print(self.board[int(col)][int(row)] + " |")
                else:
                    print("" + self.board[int(col)][int(row)], end=" ")
        print("\t\t---------")

    def rotate_anticlock(self):
        transposed = list(zip(*self.test_board))
        self.board = list(map(list, transposed[::-1]))

    def rotate_clockwise(self):
        transposed = list(zip(*reversed(self.board)))
        self.test_board = list(map(list, transposed))

    def user_input(self):
        self.print_board()
        valid = False
        self.rotate_clockwise()
        while not valid:
            user = input("It's {} turn. Enter the coordinates in (x y) format: ".format(self.player))
            _row, _col = user.split()
            if _row.isdecimal() and _col.isdecimal():
                if 3 >= int(_col) >= 1 and 3 >= int(_row) >= 1:
                    row = int(_row) - 1
                    col = int(_col) - 1
                    if self.test_board[int(row)][int(col)] not in ["_", " "]:
                        valid = False
                        print("Already value there")
                    else:
                        valid = True
                        self.test_board[int(row)][int(col)] = self.player
                        self.rotate_anticlock()
                else:
                    print(_row, _col)
                    print("Coordinates should be from 1 to 3!")
                    valid = False
            else:
                print("You should enter numbers!")
                valid = False

    def main_input(self):
        self.input = list(input("Enter cells: "))
        self.board = [self.input[:3], self.input[3:6], self.input[6:9]]
        return self.input, self.board

    def win(self):
        winner = []
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                winner.append(self.board[0][col])

        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != " ":
                winner.append(self.board[row][0])

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            winner.append(self.board[0][0])


        elif self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            winner.append(self.board[0][2])

        if len(winner) > 1:
            self.game_state = "Impossible"

        elif len(winner) == 1:
            self.game_state = winner[0] + " wins"
            self.gamedone = True
        elif self.finished():
            self.gamedone = True
            self.game_state = "Draw"
            

    def game_loop(self):
        while not self.gamedone:
            os.system('clear')
            self.print_header()
            self.user_input()
            self.win()
            if self.gamedone:
                self.print_board()
                print(self.game_state)
                break
            else:
                self.next_turn()

    def finished(self):
        for row in range(3):
            for col in range(3):
                if self.board[col][row] != "X" and self.board[col][row] != "O":
                    return False
                    break
        return True


game = TicTacToe()
game.game_loop()
