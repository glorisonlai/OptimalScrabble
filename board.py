#board is 15/15
# class Board:
#     class Tile:
#         def __init__(self,letter, pos):
#             self.Letter = letter
#             self.Pos = pos
#
#     def __init__(self):
#         width, height = 15,15

class Board:
    board_rows = 4
    board_cols = 4 #4x4 board

    class Tile:
        def __init__(self,letter, pos):
            self.Letter = letter
            self.Pos = pos
            self.Potential = []

    def __init__(self):
        self.board_state = [[None for i in range(self.board_cols)] for j in range(self.board_rows)]
        self.state = []

    def update_board(self):
        new_word = self.state[-1]
        pos = list(new_word[0])
        hori = new_word[1]
        text = list(new_word[2])

        while len(text) > 0: #Repeat until word is done
            self.board_state[pos[0]][pos[1]] = self.Tile(text.pop(0),pos) #Remove first item of word
            if hori == True:
                pos[1] += 1
            else: pos[0] += 1

    def update_state(self,args):
        for arg in args:
            try:
                assert (type(arg[0]) == tuple and type(arg[1]) == bool and type(arg[2]) == str)
                self.state.append(arg)
                self.update_board()
            except (AssertionError):
                print( type(arg[0]),type(arg[1]),type(arg[2]) )

    def show_board(self):
        for line in self.board_state:
            print_line = line
            for i in range(len(print_line)):
                tile = print_line[i]
                if tile != None:
                    print_line[i] = tile.Letter
            print(print_line)


if __name__ == "__main__":
    game = Board()
    game.update_state([ [(1,1),True,"at"] ])
    game.show_board()
